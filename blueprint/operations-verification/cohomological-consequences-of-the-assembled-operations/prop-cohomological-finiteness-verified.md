+++
id = "prop-cohomological-finiteness-verified"
kind = "theorem"
title = "Verification of Compact-support finiteness and Frobenius"
order = 3977
tags = ["latex:proposition"]
uses = ["def-weil-local-frobenius-trace", "prop-cohomological-finiteness", "prop-weil-operations", "thm-weil-cohomological-finiteness"]
+++
The interface [prop-cohomological-finiteness] of the framework chapter is verified as follows.

## Proof

The $\RGamma$ and $\RGammac$ constructions and their
Frobenius-equivariant realizations are supplied by
[prop-weil-operations]. The local normalization used for the induced
operator is the one in [def-weil-local-frobenius-trace].
Apply [thm-weil-cohomological-finiteness] to the chosen Weil complex:
it gives finite-dimensional ordinary and compact-support cohomology, a
finite vanishing interval, and a functorial geometric-Frobenius
automorphism. When $Y_0$ is proper, its proper clause gives the
Frobenius-equivariant comparison $H_c^i(Y,K)\simeq H^i(Y,K)$.
For the constant sheaf on a scheme of dimension $e$, the same theorem
gives vanishing for $i<0$ and $i>2e$, and for a geometrically connected
scheme it gives $H^0\simeq E$ with Frobenius acting as the identity.
Specializing $E$ to $\Ql$, $Y_0$ to the fixed smooth proper
geometrically connected $X_0$, and $e=d$ gives exactly the final
cohomological range and $H^0(X,\Ql)\simeq\Ql$ asserted here.
