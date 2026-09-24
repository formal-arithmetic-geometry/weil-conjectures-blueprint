+++
id = "thm-pod-point-perfectness"
kind = "theorem"
title = "Point perfectness of global sections"
order = 3806
uses = ["conventions-coefficient-categories-and-basic-operations", "def-pod-perfect-point-complex", "def-weil-algebraically-closed-coefficients", "def-weil-derived-complete-integral-detailed", "def-weil-finite-coefficient-point", "def-weil-finite-tor-amplitude", "def-weil-finite-torsion-constructibility", "def-weil-ordinary-compact-cohomology", "def-weil-rationalization-karoubi", "lem-weil-pbc-reconstruction-uniform-tower", "prop-trf-compact-support-perfectness"]
+++
In the Poincare duality conventions of this chapter (the fixed setting), $K\in D^b_{ctf}(X,\Lambda )$ with $\Lambda$ a coefficient stage of the datum. Then

$$
R\Gamma (X,K),\qquad R\Gamma _c(X,K),\qquad R\Gamma _c(X,K)^\vee
$$

are perfect point complexes at every coefficient stage: at finite level they are bounded with finite cohomology modules and finite Tor-amplitude; at the $\mathcal O_E$-stage the reductions are perfect with one common amplitude; and at the $E$- and $\overline{\mathbf Q}_{\ell }$-stages the complexes are bounded with finite-dimensional cohomology. (Source: the finiteness theorems of etale cohomology, Milne, Lectures on Etale Cohomology, Sections 19 and 29, for the finiteness and the perfectness at the point. The finite-level compact-support membership $R\Gamma _c(X,K)\in D^b_{\mathrm{fin}}(A)$ is recorded in [prop-trf-compact-support-perfectness], [prop-trf-compact-support-perfectness].)

## Proof

Step 1: the finite level. For $\Lambda=A=A_{E,n}$ and
$K\in D^b_{ctf}(X,A)$, $R\Gamma_c(X,K)\in D^b_{ctf}(s,A)$ and the
$\mathcal H^r(R\Gamma_c(X,K))$ are finite $A$-modules, by the
compact-support perfectness of [prop-trf-compact-support-perfectness],
[prop-trf-compact-support-perfectness], together with the
constructibility and finite-Tor-amplitude of $K$
([def-weil-finite-torsion-constructibility],
[def-weil-finite-tor-amplitude]); the same holds for
$R\Gamma(X,K)$ by the proper comparison $R\Gamma_c=R\Gamma$ of
[conventions-coefficient-categories-and-basic-operations] ([def-weil-ordinary-compact-cohomology]). A bounded
complex over the Noetherian ring $A$ with finite cohomology admits a
bounded-above finite free resolution $P^\bullet$: construct successive
finite sets of generators for cycles and kernels, using Noetherianity
at each step. If its Tor-amplitude is $[a,b]$, replace $P^\bullet$
by the quotient truncation in degrees $\geq a$. All terms above
$a$ remain finite free. The term
$Q=\operatorname{coker}(P^{a-1}\to P^a)$ is finitely presented.
For every $A$-module $M$, the resolution in degrees $\leq a$
identifies $\operatorname{Tor}_1^A(Q,M)$ with the degree $a-1$
cohomology of $P^\bullet\otimes_A M$, which vanishes by the
Tor-amplitude bound. Hence $Q$ is flat, and finitely presented flat
modules are projective. This gives the required bounded finite
projective representative. This elementary homological argument is
also the proof of [Stacks
Project, Tag 0658](https://stacks.math.columbia.edu/tag/0658); it does not assert that arbitrary finite
$A$-modules have finite projective dimension.
Hence $R\Gamma(X,K)$, $R\Gamma_c(X,K)$, $R\Gamma_c(X,K)^\vee$ are
perfect point complexes in the sense of
[def-pod-perfect-point-complex]. Step 2: the $\mathcal O_E$-stage.
For $K\in D^b_{ctf}(X,\mathcal O_E)$ (derived complete, by
[def-weil-derived-complete-integral-detailed]), the reductions
$K_n=K\otimes^L_{\mathcal O_E}A_{E,n}$ are perfect at finite level by
Step 1 with one common Tor-amplitude interval (the interval of
[def-weil-finite-tor-amplitude] for $K$), and the realization
under the uniform-tower reconstruction of
[lem-weil-pbc-reconstruction-uniform-tower] places
$R\Gamma_c(X,K)$ in $D^b_{\mathrm{fg}}(\mathcal O_E)$ with perfect
reductions of one common amplitude, i.e. it is a perfect point complex
at the $\mathcal O_E$-stage by [def-pod-perfect-point-complex]
and [def-weil-finite-coefficient-point]. Step 3: the field
stages. For $\Lambda=E$, the object is the rationalization
$K\otimes^L_{\mathcal O_E}E$ of an
$\mathcal O_E$-object ([def-weil-rationalization-karoubi]), whose
cohomology is finite-dimensional over $E$ by Step 2 jointly with
$\mathcal O_E\to E$ being flat; boundedness is inherited. For
$\Lambda=\Qlb$, the object is represented at a finite stage $E/\Ql$
by [def-weil-algebraically-closed-coefficients] and is therefore
bounded with finite-dimensional cohomology, as well. Step 4: the
dual. The dual $R\Gamma_c(X,K)^\vee$ of a bounded complex of finite
projective $A$-modules is a bounded complex of finite projective
modules (termwise duals), so the displayed triple is perfect at every
stage ([def-pod-perfect-point-complex]); the finite-dimensionality
at the field stages is the ordinary dual of a finite-dimensional
space.
