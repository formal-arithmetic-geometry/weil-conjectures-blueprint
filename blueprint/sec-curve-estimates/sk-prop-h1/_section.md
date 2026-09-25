+++
id = "sk-prop-h1"
kind = "section"
title = "$H^1$ via Kummer"
order = 929
uses = ["sk-def-br", "sk-def-kummer", "sk-def-pic", "sk-prop-kummer-exact", "sk-thm-br"]
+++
*Proposition (sketch).*

For $C$ as in [sk-def-curve] and every $n\ge1$ prime to
$\operatorname{char}k$:

$$
H^1(C,\mu_n)\cong\Pic(C)[n].
$$

## Proof

The sequence of [sk-def-kummer] is exact by
[sk-prop-kummer-exact] (here $n$ is prime to
$\operatorname{char}k$), so it has a long exact cohomology sequence,
which reads

$$
0\to\mu_n(k)\to k^\times\xrightarrow{n}k^\times
\to H^1(C,\mu_n)\to\Pic(C)\xrightarrow{n}\Pic(C)
\to H^2(C,\mu_n)\to H^2(C,\mathbb G_m)=\Br(C),
$$

where $k^\times\to k^\times$, $x\mapsto x^n$, is surjective ($k$
algebraically closed) and $H^1(C,\mathbb G_m)=\Pic(C)$ by
[sk-def-pic]. The last term is $0$ by [sk-thm-br], so exactness
gives $H^1(C,\mu_n)=\ker(n:\Pic(C)\to\Pic(C))=\Pic(C)[n]$.

Uses: [sk-def-br], [sk-def-kummer], [sk-def-pic], [sk-prop-kummer-exact], [sk-thm-br]
