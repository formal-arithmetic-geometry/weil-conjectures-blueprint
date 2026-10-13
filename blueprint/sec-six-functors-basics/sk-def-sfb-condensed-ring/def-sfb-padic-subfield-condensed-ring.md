+++
id = "def-sfb-padic-subfield-condensed-ring"
kind = "definition"
title = "The condensed ring $\\underline E$ of a subfield $E\\subseteq\\overline{\\mathbf Q}_\\ell$"
order = 1527
uses = ["def-sfb-continuous-map-condensed-ring", "def-sfb-continuous-map-condensed-ring-map", "def-sfb-padic-condensed-ring"]
lean = ["Profinite.padicSubfieldCondensedRing"]
+++
Let $\ell$ be a prime and $\Qlb$ an algebraic closure of $\mathbf Q_\ell$, with the
absolute value $|\cdot|$ extending that of $\mathbf Q_\ell$. Let $E$ be a field with an
embedding $\iota\colon E\hookrightarrow\Qlb$. Give $E$ the absolute value
$|x|_E:=|\iota(x)|$ and the topology it defines, which is the topology restricted from
$\Qlb$ along $\iota$. The condensed ring $\underline E$ is the condensed ring of
[def-sfb-continuous-map-condensed-ring] for this topological field:

$$
\underline E(S)=C(S,E).
$$

Its underlying ring object is commutative. If moreover $E$ is an extension of
$\mathbf Q_\ell$ and $\iota$ is $\mathbf Q_\ell$-linear, then postcomposition with
$\mathbf Q_\ell\to E$ ([def-sfb-continuous-map-condensed-ring-map]) gives a morphism of
condensed rings $\underline{\mathbf Q}_\ell\to\underline E$
([def-sfb-padic-condensed-ring]).
