+++
id = "sbc-thm-universal-test-vanishing"
kind = "theorem"
title = "Vanishing in the universal curve test"
order = 1467
uses = ["def-sbc-normal-dominant-galois", "def-sbc-smooth-morphisms", "def-weil-pbc-scheme-conventions", "sbc-def-base-change-square", "sbc-lem-etale-over-normal", "sbc-lem-higher-direct-image-presheaf", "sbc-lem-slicing", "sbc-prop-torsors-h1", "sbc-thm-algebraically-closed-invariance", "sbc-thm-cohomological-dimension-of-an-affine-curve", "sbc-thm-spreading-finite-etale-galois"]
+++
Let

$$
\begin{array}{ccc}
X & \xleftarrow{\;h\;} & Y\\
f\big\downarrow & & \big\downarrow e\\
S & \xleftarrow{\;g\;} & \operatorname{Spec}K
\end{array}
$$

be a base-change square where
$X\to S$ is an affine smooth morphism of relative dimension one (in
the sense of [def-sbc-smooth-morphisms]) and $X$ is affine, $S$ is
the spectrum of a
normal domain $A$ with
algebraically closed fraction
field $L$, and $K/L$ is an extension of algebraically closed fields.
Let $d$ be an integer invertible on $S$. Then

$$
R^qh_*(\mathbf Z/d\mathbf Z)=0\qquad(q\geq1).
$$
