from expects import expect, have_property, be_a
from expects.matchers.built_in import equal
from injector import Injector, Binder, Module, provider
from pytest import fixture, raises
from pytest_describe import behaves_like

from .simple import Config, DevConfig, Foo, foo


def describe_object():
    def default_implementation():
        def it_uses_default_implementation(subject):
            expect(subject.config).to(be_a(Config))
            expect(subject.config).not_to(be_a(DevConfig))
            expect(subject).to(have_property("config", have_property("cfg", "default")))

    def dev_implementation():
        def it_uses_dev_impl(subject):
            expect(subject.config).to(be_a(Config))
            expect(subject.config).to(be_a(DevConfig))
            expect(subject).to(have_property("config", have_property("cfg", "dev")))

    def describe_with_no_di():
        def it_fails_to_init():
            with raises(TypeError):
                Foo()

    def describe_injector_is_used():
        @fixture
        def subject(injector):
            return injector.get(Foo)

        @fixture
        def injector(modules):
            return Injector(modules)

        @behaves_like(default_implementation)
        def describe_when_using_default_injector():
            @fixture
            def modules():
                return []

        def describe_when_using_binder():
            @behaves_like(dev_implementation)
            def describe_when_module_is_a_function():
                @fixture
                def modules():
                    def configure(binder: Binder):
                        binder.bind(Config, to=DevConfig)

                    return [configure]

            @behaves_like(dev_implementation)
            def describe_when_module_is_a_class():
                @fixture
                def modules():
                    class Configure(Module):
                        def configure(self, binder: Binder):
                            binder.bind(Config, to=DevConfig)

                    return [Configure]

            @behaves_like(dev_implementation)
            def describe_when_module_uses_provider():
                @fixture
                def modules():
                    class Configure(Module):
                        @provider
                        def name_does_not_matter(self) -> Config:
                            return DevConfig()

                    return [Configure]


def describe_class():
    def default_implementation():
        def it_uses_default_implementation(subject):
            expect(subject).to(equal("default"))

    def dev_implementation():
        def it_uses_dev_impl(subject):
            expect(subject).to(equal("dev"))

    def describe_with_no_di():
        def it_fails_to_init():
            with raises(TypeError):
                foo()

    def describe_injector_is_used():
        @fixture
        def subject(injector):
            return injector.call_with_injection(foo)

        @fixture
        def injector(modules):
            return Injector(modules)

        @behaves_like(default_implementation)
        def describe_when_using_default_injector():
            @fixture
            def modules():
                return []

        def describe_when_using_binder():
            @behaves_like(dev_implementation)
            def describe_when_module_is_a_function():
                @fixture
                def modules():
                    def configure(binder: Binder):
                        binder.bind(Config, to=DevConfig)

                    return [configure]

            @behaves_like(dev_implementation)
            def describe_when_module_is_a_class():
                @fixture
                def modules():
                    class Configure(Module):
                        def configure(self, binder: Binder):
                            binder.bind(Config, to=DevConfig)

                    return [Configure]

            @behaves_like(dev_implementation)
            def describe_when_module_uses_provider():
                @fixture
                def modules():
                    class Configure(Module):
                        @provider
                        def name_does_not_matter(self) -> Config:
                            return DevConfig()

                    return [Configure]
