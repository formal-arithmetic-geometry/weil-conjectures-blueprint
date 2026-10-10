+++
id = "prop-weil-pbc-koszul-reconstruction"
kind = "theorem"
title = "Koszul and quotient reconstruction"
order = 1248
uses = ["def-weil-pbc-adic-coefficient-datum"]
tags = ["latex:proposition"]
+++
For the strict quotient tower $K_\bullet$ of
[def-weil-pbc-adic-coefficient-datum] there is a functorial isomorphism

$$
 K^{\wedge}_{\mathrm{Kos}}\xrightarrow{\sim}\Rlim K_\bullet
$$

carrying the Koszul completion map to the quotient-tower completion map
$K\to\Rlim K_\bullet$. Every derived $I$-complete object consequently
satisfies

$$
 K\xrightarrow{\sim}\Rlim K_\bullet.
$$

## Proof

This is the recorded classical input of the statement, the derived-completion
formalism of Stacks Project, More on Algebra, Section 15.93 (Tag
[091N](https://stacks.math.columbia.edu/tag/091N)): the Koszul-derived
completion of a complex and the derived limit over its strict quotient tower
compute the same object, and both completion maps are the canonical ones. The
blueprint uses the identification as the defining property of the adic
coefficient datum of [def-weil-pbc-adic-coefficient-datum] and gives no
separate proof.
