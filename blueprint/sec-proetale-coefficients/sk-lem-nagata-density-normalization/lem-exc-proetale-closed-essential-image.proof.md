+++
kind  = "proof"
of    = "lem-exc-proetale-closed-essential-image"
+++
Evaluation on an object of the open complement gives $j^*i_*G=0$, by
[lem-exc-closed-localization], since its closed fibre is empty. Conversely
suppose $j^*F=0$ and consider the unit $\eta:F\to i_*i^*F$ of the pro-etale
operations. Its closed inverse image is an isomorphism: the triangle
identity says that $i^*\eta$, followed by the counit, is the identity, and
the counit is an isomorphism by [lem-exc-proetale-closed-fully-faithful].
Its open inverse image is the map between two zero sheaves. Both inverse
images are exact by the exactness of the pro-etale module inverse image
([det-prop-sfb-module-pullback-exact-main]), so the kernel and cokernel of $\eta$ have zero open and closed
inverse images. [lem-exc-open-closed-detection] makes them zero. This proves
the unit isomorphism and the essential-image assertion.
