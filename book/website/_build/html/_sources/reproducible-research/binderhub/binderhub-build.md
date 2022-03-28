(rr-binderhub-build)=
# Build your own BinderHub

[mybinder.org](https://mybinder.org/) is the free, public BinderHub that hosts almost 100k Binder launches per week.
Why might you want to build your own?

Binder [{term}`def<Binder>`] is an open source project maintained by volunteers and as such they ask that users stay within certain computational limitations in order to keep running costs as low as possible whilst still providing a usable service.
By hosting your own BinderHub, you can offer your users much more flexible and tailored resources.

These customisations could include:

- authentication,
- greater computational resources per user,
- bespoke library stacks and packages,
- allowing access to private repos,
- persistent storage for users,
- restrict sharing within a certain institution or team.

## Issues you may face when deploying a BinderHub

BinderHubs are becoming increasingly popular amongst universities and research institutes.
This is because they can facilitate multiple instances of the same set of notebooks for use in a tutorial or workshop setting.

If you are deploying a cloud-hosted BinderHub on behalf of your organisation, you may need specific permissions on your organisation's cloud platform subscription.
Which permissions you require will vary based on the cloud platform you have access to and your IT Services policies.
At minimum, you'll need to be able to assign [Role Based Access Control (RBAC)](https://docs.microsoft.com/en-us/azure/role-based-access-control/overview) to your resources so they can act autonomously in order to manage user traffic.
