+++
id = "lem-trf-exceptional-projection-formula"
kind = "lemma"
title = "Exceptional projection formula: $f^!$ is $f^*$-linear up to the twist"
order = 2433
uses = ["def-trf-admissibility", "def-trf-categorical-trace", "def-trf-coefficient-conventions", "def-weil-derived-pullback-tensor-hom", "def-weil-finite-tor-amplitude", "def-weil-site-perfect-complex", "lem-trf-chain-supertrace", "prop-functor-package"]
+++
Fix the coefficient
conventions, $A=A_{E,n}$, let $f:X\to Y$ be a separated
finite-type morphism of finite-type $k$-schemes, admissible at $A$
([def-trf-admissibility]), and let

$$
B\in D^b_{ctf}(Y,A),\qquad
K\in D^b_{ctf}(Y,A)\cap D^b_{\mathrm{perf}}(Y,A)
$$

(site-perfect, hence dualizable
with respect to $-\otimes_A^L-$; in particular $K=A_Y$ is allowed).
Then there is a canonical $A$-linear natural isomorphism

$$
f^!(B\otimes_A^LK)\xrightarrow{\ \sim\ }f^!(B)\otimes_A^Lf^*K,
$$

the *exceptional projection formula* (equivalently the
``$f^!$ is $f^*$-linear up to the twist'' form; for $B=A_Y$ it
reads $f^!(K)\cong f^!(A_Y)\otimes_A^Lf^*K$).

## Proof

The local finite-free representatives in [def-weil-site-perfect-complex]
give evaluation and coevaluation satisfying the two triangle identities.
For every test object $C\in D^b_{ctf}(X,A)$, consider

$$
\begin{aligned}
\operatorname{Hom}_X\bigl(C,f^!(B)\otimes_A^Lf^*K\bigr)
&\xrightarrow{\ \sim\ }
\operatorname{Hom}_X\bigl(C\otimes_A^L(f^*K)^\vee,f^!B\bigr)\\
&\xrightarrow{\ \sim\ }
\operatorname{Hom}_X\bigl(C\otimes_A^Lf^*(K^\vee),f^!B\bigr)\\
&\xrightarrow{\ \sim\ }
\operatorname{Hom}_Y\bigl(f_!(C\otimes_A^Lf^*K^\vee),B\bigr)\\
&\xrightarrow{\ \sim\ }
\operatorname{Hom}_Y\bigl(f_!C\otimes_A^LK^\vee,B\bigr)\\
&\xrightarrow{\ \sim\ }
\operatorname{Hom}_Y\bigl(f_!C,B\otimes_A^LK\bigr)\\
&\xrightarrow{\ \sim\ }
\operatorname{Hom}_X\bigl(C,f^!(B\otimes_A^LK)\bigr).
\end{aligned}
$$

The arrows use, in order, dualizability, preservation of the dual by
the monoidal pullback, the exceptional adjunction of
[def-trf-admissibility], the projection formula of
[prop-functor-package], dualizability, and the same adjunction.
By the Yoneda lemma (the two displayed functors of $C$ are the
representables of the two objects, all steps being natural in $C$),
the objects $f^!(B)\otimes_A^Lf^*K$ and $f^!(B\otimes_A^LK)$ are
canonically isomorphic, which is the assertion. The naturality in
$(B,K,f)$ and the compatibility with shifts, scalar extension and
distinguished triangles are the corresponding properties of the six
steps.
*Step 1: the two ``dual'' moves.* For a dualizable object $W$
of the symmetric monoidal closed category $D^b_{\mathrm{fin}}(A)$
(and its local/global analogues) one has the canonical isomorphism

$$
R\mathcal Hom_A(W^\vee,-)\xrightarrow{\ \sim\ }-\otimes_A^LW,
\qquad \text{hence}\qquad
\operatorname{Hom}_D(C\otimes_A^LW^\vee,Z)
\xrightarrow{\ \sim\ }\operatorname{Hom}_D(C,Z\otimes_A^LW),
$$

the tensor–internal-Hom adjunction combined with the duality data
$(\operatorname{coev}_W,\operatorname{ev}_W)$ of
[def-trf-categorical-trace] (the model-level verification of the
triangle identities is [lem-trf-chain-supertrace]); applying
this with $W=f^*K$ (dualizable, as the monoidal functor $f^*$ of
[def-weil-derived-pullback-tensor-hom] preserves dualizable
objects and duals: apply $f^*$ to the evaluation and coevaluation
of $K$; monoidality preserves their two triangle identities,
so $f^*(K^\vee)$ is a dual of $f^*K$) and with $W=K$ gives the first
and the fifth arrows of the chase, respectively.

*Step 2: the middle moves.* The third arrow is the adjunction
$f_!\dashv f^!$ of [def-trf-admissibility] applied to the
object $C\otimes_A^Lf^*K^\vee$; the fourth is the projection
formula

$$
f_!(X\otimes_A^Lf^*Y)\xrightarrow{\ \sim\ }f_!X\otimes_A^LY
$$

of [prop-functor-package], item (5), with
$X=C$, $Y=K^\vee$; the fifth is again the first move with
$W=K$, giving $R\mathcal Hom_A(K^\vee,-)\cong-\otimes_A^LK$; the
last is the adjunction applied to $C$.

*Step 3: the Yoneda step.* The isomorphisms of Steps 1–2 are
all natural in $C$, so they supply a natural isomorphism between
the two representable functors $\operatorname{Hom}(C,-)$ of the
candidate objects; the Yoneda lemma for the derived categories (whose
morphism sets are the sets of natural transformations between the
representable functors of two objects of a triangulated category,
$\operatorname{Hom}_D(C,(-))$ being a functor
$D^{\mathrm{op}}\to\mathrm{Set}$ that is representable by its
object) gives the canonical isomorphism
$f^!(B)\otimes_A^Lf^*K\cong f^!(B\otimes_A^LK)$. Naturality in
$(B,K,f)$ and the stated compatibilities are the naturality of the
six steps.
