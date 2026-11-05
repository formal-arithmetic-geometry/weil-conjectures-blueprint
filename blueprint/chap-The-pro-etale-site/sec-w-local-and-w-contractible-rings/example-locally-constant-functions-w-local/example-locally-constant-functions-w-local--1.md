+++
id = "example-locally-constant-functions-w-local--1"
kind = "example"
title = "Finite quotients and the spectrum"
name_showing = false
order = 48001
aliases = ["bp-r009-1"]
lean = ["LocallyConstant.discreteQuotientColimitPresentation", "LocallyConstant.homeomorphPrimeSpectrum"]
uses = []
+++
Let $A$ be a commutative ring and let $S$ be a compact topological
space. The finite discrete quotients $Q$ of $S$, ordered by refinement,
give a filtered colimit of $A$-algebras
$$
LC(S,A)=\varinjlim_Q A^Q,
$$
whose structure maps are pullback along $S\to Q$.

If $S$ is profinite, evaluation gives a homeomorphism
$$
S\times\operatorname{Spec}(A)\xrightarrow{\ \sim\ }
\operatorname{Spec}(LC(S,A)),\qquad
(s,\mathfrak p)\longmapsto\{f\mid f(s)\in\mathfrak p\}.
$$
In particular, for any field $k'$ the spectrum of $LC(S,k')$ is $S$,
and $s$ corresponds to the maximal ideal of functions vanishing at $s$.

*Proof.* On a discrete quotient $Q$, locally constant functions are all functions
$Q\to A$. Every locally constant function on $S$ factors through the
quotient by its fibres, which is finite by compactness. Pullback from
any quotient is injective because $S\to Q$ is surjective. These two
facts verify the filtered colimit property on underlying sets, hence
on $A$-algebras.

Write $\Phi(s,\mathfrak p)=\{f\mid f(s)\in\mathfrak p\}$. This is a
prime ideal, and $\Phi$ is continuous: near $(s,\mathfrak p)$ the
condition $f(s)\notin\mathfrak p$ is constant in the $S$-coordinate
and is a basic open condition in $\operatorname{Spec}(A)$.

For a prime ideal $P$ of $LC(S,A)$, consider the clopen subsets $U$ of
$S$ whose characteristic functions $\chi_U$ do not belong to $P$.
They form a family of nonempty closed sets stable under finite
intersections. Compactness gives a point $s$ in their intersection.
The identities $\chi_U\chi_{U^c}=0$ and $\chi_U+\chi_{U^c}=1$ imply
that $\chi_U\notin P$ whenever $s\in U$, and then that every function
vanishing at $s$ lies in $P$. Subtracting the constant function with
value $f(s)$ shows that $P=\Phi(s,\mathfrak p)$, where $\mathfrak p$
is the contraction of $P$ to $A$. Thus $\Phi$ is surjective.

Contraction recovers $\mathfrak p$, and clopen subsets separate distinct
points of the profinite set $S$, so $\Phi$ is injective. Finally, for
$U$ clopen and $a\in A$, the image of $U\times D(a)$ is
$D(\chi_Ua)$. These sets form bases, so $\Phi$ is open and hence a
homeomorphism. For a field, its spectrum consists of the zero ideal,
giving the last assertion.
