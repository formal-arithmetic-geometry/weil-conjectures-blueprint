+++
id = "prop-coefficient-passage"
kind = "theorem"
title = "Adic, rational, and algebraically closed passage"
order = 1859
tags = ["latex:proposition"]
uses = ["def-exchange-projection", "def-weil-algebraically-closed-coefficients", "def-weil-derived-complete-integral-detailed", "def-weil-derived-direct-image", "def-weil-derived-pullback-tensor-hom", "def-weil-finite-field-fiber", "def-weil-finite-torsion-constructibility", "def-weil-pbc-proetale-site", "def-weil-rationalization-karoubi", "def-weil-scheme-morphism-properties", "prop-weil-direct-image-constructible-landing", "prop-weil-finite-proper-base-change-exchange", "prop-weil-pbc-direct-image-limits", "prop-weil-pbc-rational-transport", "thm-weil-pbc-finite-extension", "thm-weil-pbc-qbar"]
+++
Fix a prime $p$, an integer $a\in\mathbf Z_{\geq1}$, put
$q=p^a$, $k_0=\Fq$, and let $k=\Fbar$ be the
fixed algebraic closure of $k_0$.
Choose a prime $\ell\neq p$, write $\Ql=\mathbf Q_\ell$, and choose an
algebraic closure $\Qlb$ of $\Ql$. Let $E/\Ql$ be finite with valuation ring
$\mathcal O_E$ and uniformizer $\varpi_E$. Let $S$ be a scheme on
which $\ell$ is invertible, let $X,Y$ be
finite-type $S$-schemes, and
let $f:X\to Y$ be a
proper $S$-morphism.
For $K\in D^b_c(X,\mathcal O_E)$, a
derived-complete integral
complex with bounded constructible reductions, set

$$
A_{E,n}=\mathcal O_E/\varpi_E^n,\qquad
K_n=K\otimes^L_{\mathcal O_E}A_{E,n}\quad(n\geq1).
$$

The rings $A_{E,n}$ are the
finite-torsion coefficient
rings.
The functors $Rf_*$ and $Rf_{*,n}$ are the
derived direct images on the
small pro-etale sites. Let the diagram

$$
\begin{array}{ccc}
X'&\xrightarrow{g'}&X\\
f'\downarrow&&\downarrow f\\
Y'&\xrightarrow{g}&Y
\end{array}
$$

be a Cartesian square of
finite-type $S$-schemes
with four
separated finite-type
$S$-arrows. The symbols $Lg^*$ and $Lg'^*$ use the
derived pullback notation.
The exchange map
$\operatorname{Ex}_*(K):Lg^*Rf_*K\to Rf'_*Lg'^*K$ is an isomorphism when
$f$ is proper and is compatible with reduction of coefficients. Then

$$
(Rf_*K)\otimes^L_{\mathcal O_E}A_{E,n}
\xrightarrow{\sim}Rf_{*,n}K_n
$$

for every $n\geq1$, and

$$
Rf_*K\xrightarrow{\sim}
R\varprojlim_n\operatorname{Res}_nRf_{*,n}K_n.
$$

The reduction of $\operatorname{Ex}_*(K)$ is
$\operatorname{Ex}_*(K_n)$. The exactness and constructibility of the
derived direct image at every coefficient level is the statement of
[prop-weil-direct-image-constructible-landing]; the exchange map
$\operatorname{Ex}_*$ is an isomorphism for
proper
$f$ by [prop-weil-finite-proper-base-change-exchange].
(*Source: the coefficient-passage chain of the $\ell$-adic
formalism for proper direct images, from finite-torsion to
derived-complete integral, rational and algebraically closed levels, in
the derived-complete pro-etale presentation, cf. Stacks Project,
Pro-etale Cohomology, Section 61.30, Theorem 61.30.1, Tag
`09C9`.*)

## Proof

The adic, rational, and algebraically closed coefficient passage for
proper direct images is decomposed in the proper-base-change chapter: the inverse-limit
statement is [prop-weil-pbc-direct-image-limits], the rational
transport [prop-weil-pbc-rational-transport], the finite-extension
passage [thm-weil-pbc-finite-extension], and the algebraically
closed coefficient category thm:weil-pbc-qbar.
