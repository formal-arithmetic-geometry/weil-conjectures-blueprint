+++
id = "lem-weil-pbc-injective-restriction-acyclicity"
kind = "lemma"
title = "Acyclicity bound for restricted injectives"
order = 1546
uses = ["def-weil-pbc-henselian-terminology", "def-weil-pbc-scheme-conventions", "prop-weil-pbc-gabber-affine-comparison-detailed"]
+++
Let $(A,I)$ be an affine henselian pair, let $Y$ be separated of finite type
over $\operatorname{Spec}A$ with affine diagonal, covered by $n+1$ affine
opens, and let $Y_0=Y\times_{\operatorname{Spec}A}\operatorname{Spec}(A/I)$.
If $I$ is injective on $Y_{\Et}$, then

$$
 H^q(Y_0,I|_{Y_0})=0\qquad(q>n).
$$

## Proof

Each affine open $U\subseteq Y$ is affine of finite type over
$\operatorname{Spec}A$, and its closed fibre is $U_0=U\times_YY_0$, so
Gabber's affine comparison in the relative form
[prop-weil-pbc-gabber-affine-comparison-detailed] gives $H^q(U_0,I|_U)\cong
H^q(U,I|_U)$; an injective sheaf on an affine scheme has no higher cohomology,
so $H^q(U_0,I|_U)=0$ for $q>0$. This is the case $n=0$; the hypothesis that
the charts are affine over the henselian pair, and not the false assertion
that they are themselves henselian pairs, is what makes the comparison
applicable. For the induction step write $Y=U\cup V$ with $U$ affine and $V$
covered by $n$ affine opens; the intersection $U\cap V$ is affine because $Y$
is separated with affine diagonal, and the Mayer--Vietoris long exact sequence
of the closed fibre

$$
 \cdots\to H^q((U\cup V)_0,-)\to H^q(U_0,-)\oplus H^q(V_0,-)
 \to H^q((U\cap V)_0,-)\to\cdots
$$

together with the induction hypothesis for $V$ and for $U\cap V$ gives the
vanishing for $q>n$. The restriction of an injective sheaf to an open
subscheme is injective on the small etale site, so the induction hypothesis
applies to $V$, to $U\cap V$ and to each chart separately.
