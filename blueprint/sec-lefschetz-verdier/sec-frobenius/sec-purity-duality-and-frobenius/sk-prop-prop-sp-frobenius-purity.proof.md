+++
kind = "proof"
of = "sk-prop-prop-sp-frobenius-purity"
uses = ["sk-prop-sp-purity-bc"]
+++
The first identity is Proposition [sk-prop-sp-purity-bc] for this
square. Since $\operatorname{Fr}_X$ is not a morphism over $k$, the only
point to check is that the identification of twists used there is the
Kummer identification. This holds because pullback along
$\operatorname{Fr}_T$ sends the Kummer class of a unit to the Kummer class
of its pullback. The second identity follows from
the first and the counit identity defining exceptional base change, which
says that after base change for compact support, the pulled-back
counit is the counit preceded by the exceptional comparison.
