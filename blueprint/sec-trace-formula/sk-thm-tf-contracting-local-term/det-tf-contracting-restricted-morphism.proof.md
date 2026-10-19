+++
kind = "proof"
of = "det-tf-contracting-restricted-morphism"
uses = ["def-trf-correspondence"]
+++
*(1)* The ideal of $c_2^{-1}(Z)$ is $c_2^\cdot I\,\mathcal O_C$, which is contained in
$c_1^\cdot I\,\mathcal O_C$, the ideal of $c_1^{-1}(Z)$. So $c_1^{-1}(Z)\subset c_2^{-1}(Z)$ as
closed subschemes, and the reduced scheme $C_Z$ maps into $Z_{\mathrm{red}}$ under $c_2$. The
isomorphism $e^*c_2^*\simeq c_{Z,2}^*i^*$ is the composition isomorphism for
$c_2e=ic_{Z,2}$.

*(2)* The square formed by $e$, $i$, $c_1$ and $c_{Z,1}$ is Cartesian up to reduction:
$c_1^{-1}(Z_{\mathrm{red}})$ and $C_Z$ have the same reduction. Pullback to a nilpotent
thickening is an equivalence on étale sites, so compact-support base change for the Cartesian
square gives $i^*Rc_{1!}\simeq Rc_{Z,1!}e^*$.

*Equivalent description.* The base-change mate $e^*c_1^!\to c_{Z,1}^!i^*$ is the
$Rc_{Z,1!}$-adjoint of $Rc_{Z,1!}e^*c_1^!\simeq i^*Rc_{1!}c_1^!\xrightarrow{i^*\varepsilon}i^*$.
Composing with $e^*u$ and taking adjoints, the naturality of the base-change isomorphism
identifies the adjoint of the composite with $i^*(\varepsilon\circ Rc_{1!}u)=i^*\widehat u$
after the isomorphism of (2). So the two descriptions agree.
