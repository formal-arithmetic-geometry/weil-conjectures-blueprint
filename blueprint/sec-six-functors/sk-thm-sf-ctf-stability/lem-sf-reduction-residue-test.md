+++
id = "lem-sf-reduction-residue-test"
kind = "lemma"
title = "Reduction, geometric stalks, and the residue test"
order = 2336
uses = ["def-weil-derived-tensor", "def-weil-finite-tor-amplitude", "def-weil-pbc-geometric-stalks", "lem-exc-residue-tor-test", "lem-sf-flat-model", "lem-sf-stalk-free-model", "prop-weil-pbc-geometric-stalks-exact"]
+++
Let $A_{E,m}$ and $A_{E,n}$ be two finite coefficient stages with
$m\leq n$, put $\kappa_n=A_{E,n}/(\varpi_E)$ and
$\kappa_m=A_{E,m}/(\varpi_E)$, let $T$ be a scheme on which $\ell$ is
invertible, and let $K$ be a bounded complex of $A_{E,n}$-modules with
constructible cohomology on a small étale site, with reduction
$K_m=K\otimes^L_{A_{E,n}}A_{E,m}$.

1. **(i)** Reduction commutes with geometric stalks: for every
geometric point $\bar t\to T$
one has $(K_m)_{\bar t}\cong K_{\bar t}\otimes^L_{A_{E,n}}A_{E,m}$.
1. **(ii)** The finite free models of the geometric stalks therefore
reduce: if the stalk $K_{\bar t}$ is isomorphic to a bounded complex
$P$ of finite free $A_{E,n}$-modules with $P^q=0$ for
$q\notin[a,b]$, in the sense of [lem-sf-stalk-free-model], then
$(K_m)_{\bar t}\cong P\otimes_{A_{E,n}}A_{E,m}$ is a bounded complex of
finite free $A_{E,m}$-modules concentrated in $[a,b]$. At the level of
the geometric stalks, and hence of the finite free models that the residue
criterion of [lem-exc-residue-tor-test] produces from them, the input
of that criterion is therefore stable under reduction, with the same
interval.
1. **(iii)** *Warning: the residue field itself does not reduce.* For
every $m<n$ one has
$$
\kappa_n\otimes^L_{A_{E,n}}A_{E,m}\cong\bigoplus_{i\geq0}\kappa_m[i],
$$
an unbounded complex, not the residue field $\kappa_m$ in degree zero.
Consequently the residue test of [lem-exc-residue-tor-test] cannot be
transported along finite reduction by reducing its test complex
$K\otimes^L_{A_{E,n}}\kappa_n$: the two complexes
$(K\otimes^L_{A_{E,n}}\kappa_n)\otimes^L_{A_{E,n}}A_{E,m}$ and
$K_m\otimes^L_{A_{E,m}}\kappa_m$ are not isomorphic in general.

## Proof

*(i).* The geometric stalk functor is exact by
[prop-weil-pbc-geometric-stalks-exact] and commutes with the ordinary
tensor product of module sheaves, hence with the derived tensor product of
[def-weil-derived-tensor]; the same argument is used in the proof of
the finite-Tor part of the internal-Hom theorem of this chapter. Applying
it to the reduction $K_m=K\otimes^L_{A_{E,n}}A_{E,m}$, whose second
factor is a module placed in degree zero, gives (i).
*(ii).* By (i) the stalk of the reduction is
$K_{\bar t}\otimes^L_{A_{E,n}}A_{E,m}$. The complex $P$ of the
statement is bounded with free terms, hence K-flat, by the argument of
[lem-sf-flat-model], so this derived tensor product is computed by the
ordinary tensor complex $P\otimes_{A_{E,n}}A_{E,m}$, whose terms are the
finite free $A_{E,m}$-modules $P^q\otimes_{A_{E,n}}A_{E,m}$ and are
concentrated in $[a,b]$. That complex is a bounded complex of finite
free $A_{E,m}$-modules concentrated in $[a,b]$, representing the stalk
of $K_m$; the criterion [lem-exc-residue-tor-test] is stated for a
bounded complex with constructible cohomology on a small étale site and
converts the vanishing of its residue-field tensor product into finite Tor
amplitude, so it applies to $K_m$ with the interval $[a,b]$.
*(iii).* Write $A=A_{E,n}$ and $\varpi=\varpi_E$. The residue
field $\kappa_n=A/\varpi A$ has the following free resolution over $A$,
in which all terms are $A$ itself:

$$
\cdots\longrightarrow A\xrightarrow{\ \varpi^{n-1}\ }A
\xrightarrow{\ \varpi\ }A\xrightarrow{\ \varpi^{n-1}\ }A
\xrightarrow{\ \varpi\ }A\longrightarrow\kappa_n\longrightarrow0,
$$

the differentials alternating between multiplication by $\varpi$ and by
$\varpi^{n-1}$. It is a complex because
$\varpi\cdot\varpi^{n-1}=\varpi^n=0$ in $A$, and it is exact: the image
of the map into the last copy of $A$ is $\varpi A$, which is the kernel
of the augmentation, the kernel of multiplication by $\varpi$ on $A$ is
$\varpi^{n-1}A$, which is the image of the preceding multiplication by
$\varpi^{n-1}$, and the kernel of multiplication by $\varpi^{n-1}$ on
$A$ is $\varpi A$, which is the image of the preceding multiplication
by $\varpi$. Tensoring this resolution with $A_{E,m}=A/\varpi^mA$ over
$A$ turns its differentials into the same two multiplications acting on
$A_{E,m}$, and because $m<n$ the exponent $n-1$ is at least $m$, so
multiplication by $\varpi^{n-1}$ is the zero map on $A_{E,m}$ while
multiplication by $\varpi$ has kernel $\varpi^{m-1}A/\varpi^mA$ and
image $\varpi A/\varpi^mA$. The tensored complex therefore has
differentials alternating between $0$ and multiplication by $\varpi$,
and its homology in each degree is either
$\ker(\varpi)=\varpi^{m-1}A/\varpi^mA\cong A/\varpi=\kappa_m$, when the
outgoing differential is multiplication by $\varpi$ and the incoming one
is zero, or $A_{E,m}/\varpi A_{E,m}=\kappa_m$, when the outgoing
differential is zero and the incoming one is multiplication by $\varpi$;
the cokernel of the last multiplication by $\varpi$ is the same group,
so the augmented complex has $\kappa_m$ in degree zero as well. Hence
$\operatorname{Tor}^{A_{E,n}}_i(\kappa_n, A_{E,m})\cong\kappa_m$ for
every $i\geq0$ and every $m<n$, which is the displayed direct sum, and
it is unbounded, whereas
$K_m\otimes^L_{A_{E,m}}\kappa_m$ involves only the residue field
$\kappa_m$ of the reduced ring. The two complexes displayed in (iii)
have therefore different cohomological amplitudes in general, and the
residue test cannot be transported along reduction by reducing its test
complex.
