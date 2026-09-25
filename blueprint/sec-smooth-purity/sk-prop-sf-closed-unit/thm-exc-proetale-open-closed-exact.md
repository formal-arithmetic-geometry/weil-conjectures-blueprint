+++
id = "thm-exc-proetale-open-closed-exact"
kind = "theorem"
title = "The ambient open-closed short exact sequence"
order = 1902
uses = ["def-weil-extension-by-zero", "def-weil-pbc-proetale-operations", "def-weil-pbc-scheme-conventions", "lem-exc-closed-restriction-extension-zero", "lem-exc-proetale-closed-essential-image", "lem-exc-proetale-open-unit", "lem-weil-extension-by-zero-adjunction", "prop-weil-pbc-proetale-constant-exact"]
+++
Let $i:Z\hookrightarrow X$ be a closed immersion with quasi-compact
complementary open immersion $j$. For every constant-coefficient pro-etale
module sheaf $F$, the open counit and closed unit form a natural short exact
sequence
$$
 0\longrightarrow j_!j^*F\longrightarrow F
 \longrightarrow i_*i^*F\longrightarrow0.
$$
This assertion concerns all module sheaves, before constructible
restriction.

## Proof

The presheaf for $j_!j^*F$ maps injectively to $F$: it is either the
identity of $F(V)$ or the injection from zero on a test object $V$. Exact
sheafification makes $j_!j^*F\to F$ a monomorphism. By the
extension-by-zero adjunction this is the open counit. Let $Q$ be its
cokernel.

Exactness of inverse image and [lem-exc-proetale-open-unit] give $j^*Q=0$.
The same exactness and [lem-exc-closed-restriction-extension-zero] identify
the map $i^*F\to i^*Q$ with an isomorphism. By
[lem-exc-proetale-closed-essential-image], the unit $Q\to i_*i^*Q$ is an
isomorphism. Composing its inverse identification with $i^*F\simeq i^*Q$
yields $Q\simeq i_*i^*F$. The map from $F$ to this quotient is the closed
unit: naturality of the unit says
$\eta_Q\circ(F\to Q)=i_*i^*(F\to Q)\circ\eta_F$. Thus the quotient sequence
is exactly the sequence in the statement, naturally in $F$. This proves the
gluing sequence of [Stacks Project, Section
61.26](https://stacks.math.columbia.edu/tag/09AD) by lifting covers, without
invoking geometric-stalk conservativity on the pro-etale site.
