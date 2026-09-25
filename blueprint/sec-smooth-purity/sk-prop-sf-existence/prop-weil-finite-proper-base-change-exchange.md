+++
id = "prop-weil-finite-proper-base-change-exchange"
kind = "theorem"
title = "Finite-torsion proper base change"
order = 1839
tags = ["latex:proposition"]
uses = ["def-exchange-projection", "def-weil-derived-direct-image", "def-weil-derived-pullback-tensor-hom", "def-weil-finite-torsion-constructibility", "def-weil-pbc-proetale-site", "def-weil-scheme-morphism-properties"]
+++
Fix a prime $\ell$, write $\Ql=\mathbf Q_\ell$, choose an algebraic
closure $\Qlb$ of $\Ql$, and fix a finite extension $E/\Ql$ contained in
$\Qlb$, with valuation ring $\mathcal O_E$ and a uniformizer
$\varpi_E$. Let $n\in\mathbf Z_{\geq1}$, and put
$A=A_{E,n}=\mathcal O_E/\varpi_E^n$. Let $S$ be a scheme on
which $\ell$ is invertible. Let

$$
\begin{array}{ccc}
X'&\xrightarrow{g'}&X\\
f'\downarrow&&\downarrow f\\
Y'&\xrightarrow{g}&Y
\end{array}
$$

be a Cartesian square whose four schemes are
finite-type $S$-schemes and
whose four arrows are
separated finite-type
$S$-morphisms. For $K\in D^b_c(X,A)$ satisfying the
finite-torsion
constructibility condition on the
small pro-etale site, the symbols
$Lg^*$ and $Lg'^*$ use the
derived pullback notation, and
the derived direct images define the
exchange map

$$
\operatorname{Ex}_*(K):Lg^*Rf_*K\longrightarrow Rf'_*Lg'^*K.
$$

If $f$ is a
proper morphism, then
$\operatorname{Ex}_*(K)$ is an isomorphism,

$$
\operatorname{Ex}_*(K):Lg^*Rf_*K\xrightarrow{\sim}Rf'_*Lg'^*K.
$$

(*Source: the finite-torsion proper base change theorem on the
small pro-etale sites: Stacks Project, Pro-etale Cohomology, Section
61.30 (Proper base change), Theorem 61.30.1, Tag
[09C9](https://stacks.math.columbia.edu/tag/09C9), in the
finite-torsion form stated here; the formal coherence properties are
split off in [prop-weil-proper-base-change-coherence].*)

## Proof

This is the recorded classical input named in the statement, Stacks Project, Pro-etale Cohomology, Section 61.30, Theorem 61.30.1 ([Tag 09C9](https://stacks.math.columbia.edu/tag/09C9)), in the finite-torsion form stated here; the formal coherence properties of the exchange map are split off in [prop-weil-proper-base-change-coherence]. No separate proof is given.
