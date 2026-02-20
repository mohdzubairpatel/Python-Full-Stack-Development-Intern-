# Base class (not strictly required but good for structure)
class SocialMedia:
    def send_message(self, msg):
        pass  # abstract idea, will behave differently in each subclass

# Subclasses for each platform
class WhatsApp(SocialMedia):
    def send_message(self, msg):
        print(f"WhatsApp message: {msg}")

class Instagram(SocialMedia):
    def send_message(self, msg):
        print(f"Instagram DM: {msg}")

class X(SocialMedia):
    def send_message(self, msg):
        print(f"X post: {msg}")


# Using polymorphism
apps = [WhatsApp(), Instagram(), X()]

for app in apps:
    app.send_message("Hello, this is a polymorphism example!")
