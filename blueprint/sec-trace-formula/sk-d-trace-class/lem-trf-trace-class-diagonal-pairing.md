+++
id = "lem-trf-trace-class-diagonal-pairing"
kind = "lemma"
title = "The trace class is the diagonal supported pairing"
order = 2622
uses = ["def-sf-kv-maps", "def-trf-admissibility", "def-trf-correspondence", "def-trf-dualizing-complex", "def-trf-fixed-scheme", "def-trf-supported-pairing", "def-trf-trace-class", "def-trf-trace-class-source", "def-weil-derived-pullback-tensor-hom", "lem-trf-correspondence-class", "lem-trf-exceptional-internal-hom-exchange", "lem-trf-trace-map-from-external-duality", "prop-functor-package", "prop-trf-exceptional-kunneth", "thm-trf-dualizing-complex-composition", "thm-trf-fixed-point-base-change", "thm-trf-kunneth-verdier", "thm-trf-verdier-duality"]
+++
Fix the coefficient conventions, $A=A_{E,n}$, $s=\Spec k$, let
$c=(c_1,c_2):C\to X\times_sX$ be an admissible correspondence
([def-trf-correspondence]) with fixed scheme $F=\Fix(c)$ and fixed-square
maps $i_F:F\to C$, $d:F\to X$ ([def-trf-fixed-scheme]), let
$K\in D^b_{ctf}(X,A)$ and $u:Lc_2^*K\to Rc_1^!K$. Assume the exceptional
admissibility ([def-trf-admissibility]) required by
[def-trf-supported-pairing] for the diagonal opposite pair
$(C,c,u)$, $(X,\Delta_X,1_K)$ and by
[lem-trf-trace-map-from-external-duality]. Then the Borel–Moore section
of the diagonal pair ([def-trf-supported-pairing]) is the Verdier trace
class of [def-trf-trace-class]:

$$
\langle u,1_K\rangle_{\mathrm{LV}}=\Tr_c(u)
\qquad\text{in }\Hom_{D(F,A)}(A_F,\omega_{F,A}).
$$

The equality holds exactly, with no sign and no twist: both sides are
the exceptional adjoint, along $d$, of the class of $u$ read through the
Künneth–Verdier isomorphism, base changed to the diagonal and evaluated.
