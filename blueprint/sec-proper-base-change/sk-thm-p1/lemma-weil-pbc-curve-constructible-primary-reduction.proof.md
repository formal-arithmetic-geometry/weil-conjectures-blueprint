+++
kind  = "proof"
of    = "lemma-weil-pbc-curve-constructible-primary-reduction"
+++
The reduction map $r:X_{\mathrm{red}}\to X$ is a universal homeomorphism.
The site equivalence sends $F$ to $r^{-1}F$, preserves covering families, and
therefore identifies the cochain complexes computing all cohomology groups.
It also commutes with the corresponding reduction after extending $k$.

The etale topos of the noetherian scheme $X$ is coherent. Given finitely
many local sections of $F$ on quasi-compact etale objects and finitely many
relations, their image generates a constructible subsheaf: refine by a
finite stratification on which the finitely generated stalk groups are
constant. Ordered by inclusion, these constructible subsheaves $F_\lambda$
form a filtered system with $F=\varinjlim_\lambda F_\lambda$. The preceding
continuity lemma gives the natural square

$$
\begin{CD}
\varinjlim_\lambda H^q(X,F_\lambda) @>{\sim}>> H^q(X,F)\\
@VVV @VVV\\
\varinjlim_\lambda H^q(X_{k'},F_\lambda|) @>{\sim}>>
H^q(X_{k'},F|).
\end{CD}
$$

Thus comparison for every constructible $F_\lambda$ implies comparison for
$F$.

Fix a constructible $F$. A finite stratification with finite stalks gives
one exponent $N$ annihilating every stalk, hence $NF=0$. Write
$N=\prod_{\ell\mid N}\ell^{r_\ell}$. Bezout supplies integers
$e_\ell$ which are $1$ modulo $\ell^{r_\ell}$ and $0$ modulo the other prime
powers. The mutually orthogonal endomorphisms $e_\ell:F\to F$ sum to the
identity and give the explicit decomposition

$$
F\xrightarrow{\sim}\bigoplus_{\ell\mid N}F[\ell^{r_\ell}],
\qquad s\longmapsto(e_\ell s)_\ell,
$$

whose inverse is addition. It remains to treat one summand.

If $\ell^rF=0$, use the exact kernel–quotient sequence

$$
0\longrightarrow F[\ell]\xrightarrow{\iota}F
\xrightarrow{\pi}F/F[\ell]\longrightarrow0.
$$

The quotient is killed by $\ell^{r-1}$ because
$\ell^{r-1}s\in F[\ell]$. Pullback to $X_{k'}$ preserves this kernel,
quotient, and both maps. Induction on $r$, with the base case $\ell F=0$ given by the hypothesis,
and the five lemma applied to the two long exact cohomology sequences,
linked by the pullback maps (as in the short-exact devissage lemma), prove
the comparison for $F$. If $F$ is prime to $\operatorname{char}k$, so are its
constructible subsheaves, and only primes $\ell\neq\operatorname{char}k$
occur in the decomposition.
