+++
id = "lem-pur-td-kernel"
kind = "lemma"
title = "Kernel identification"
order = 3562
uses = ["def-exchange-projection", "def-pur-conventions", "def-weil-derived-pullback-tensor-hom", "def-weil-derived-tensor", "def-weil-scheme-morphism-properties", "def-weil-small-proetale-site-detailed", "thm-cbc-finite-torsion"]
+++
In the purity conventions of this chapter ([def-pur-conventions] fixed setting),
let $f:X\to Y$ be a
separated
finite-type morphism — no adjoint of $Rf_!$ occurs in the statement, so
no admissibility hypothesis is carried, the ambient datum of
def:weil-ambient-exceptional-adjoint being a theorem on the
coefficients used below in any case,
[cor-sf-ambient-adjoint-discharge] — let
$K\in D^b_{ctf}(X,\Lambda)$, and let $L\in D^b_{ctf}(X,\Lambda)$ be
tensor-invertible. With $W=X\times_YX$ and $p_1,p_2:W\to X$ the
projections, there is a canonical isomorphism

$$
Lf^*Rf_!K\otimes^L_{\Lambda_X}L
\;\xrightarrow{\ \sim\ }\;
Rp_{2!}\bigl(p_1^*K\otimes^L_{\Lambda_W}p_2^*L\bigr)
$$

in $D^b_{ctf}(X,\Lambda)$.

## Proof

Step 1: the compactly supported base change. The square

$$
\begin{array}{ccc}
W&\xrightarrow{\ p_2\ }&X\\
\big\downarrow p_1&&\big\downarrow f\\
X&\xrightarrow{\ f\ }&Y
\end{array}
$$

is Cartesian. By the compactly supported base change of
[def-exchange-projection] ([thm-cbc-finite-torsion]),

$$
Lp_2^*Rf_!K\;\xrightarrow{\ \sim\ }\;Rp_{1!}Lf^*K
\qquad\text{on }W
$$

(used in the orientation that makes the two pullbacks of $K$ agree:
$f\circ p_1=f\circ p_2$). Step 2: the projection formula. By the
projection formula of [def-exchange-projection],

$$
Rp_{1!}\bigl(p_1^*K\otimes^L_{\Lambda_W}p_2^*L\bigr)
\;\cong\;
K\otimes^L_{\Lambda_X}Rp_{1!}p_2^*L,
$$

and symmetrically, applying the same two steps to the other projection,

$$
Rp_{2!}\bigl(p_1^*K\otimes^L_{\Lambda_W}p_2^*L\bigr)
\;\cong\;
\bigl(Rp_{2!}p_1^*K\bigr)\otimes^L_{\Lambda_X}L.
$$

Step 3: the transpose. The two displayed base-change isomorphisms of
Step 1 are the same statement for the two orientations of the Cartesian
square; combining them (the identity $p_1=f^*$-pullback-compatibility
and the associativity of the derived tensor product, of
[def-weil-derived-pullback-tensor-hom] and
[def-weil-derived-tensor]) gives

$$
Rp_{2!}p_1^*K\;\cong\;Lf^*Rf_!K
$$

and hence the displayed identification.
