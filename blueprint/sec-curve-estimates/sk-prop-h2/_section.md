+++
id = "sk-prop-h2"
kind = "section"
title = "$H^2$ via Kummer"
order = 933
uses = ["sk-def-br", "sk-def-kummer", "sk-def-pic", "sk-prop-kummer-exact", "sk-thm-br"]
+++
*Proposition (sketch).*

For $C$ as in [sk-def-curve] and every $n\ge1$ prime to
$\operatorname{char}k$:

$$
H^2(C,\mu_n)\cong\Pic(C)/n\cdot\Pic(C).
$$

## Proof

In the same long exact sequence of [sk-def-kummer], exact by
[sk-prop-kummer-exact] (with
$H^1(C,\mathbb G_m)=\Pic(C)$ by [sk-def-pic] and the last term
$0$ by [sk-thm-br]) the displayed quotient is the cokernel of
$n:\Pic(C)\to\Pic(C)$.

Uses: [sk-def-br], [sk-def-kummer], [sk-def-pic], [sk-prop-kummer-exact], [sk-thm-br]
