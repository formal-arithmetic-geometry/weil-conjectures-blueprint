+++
kind = "proof"
of = "proposition-inverting-ell--1"
order = 303002
+++
Both assertions are [bhatt-scholze15, Proposition 6.8.14(2)]. We prove the first,
which is where the Noetherian hypothesis enters. Let $K\in\Dbc(X,\mathcal O_E)$.
By Definition [definition-constructible-sheaves], there is a finite stratification such
that the restriction of each of the finitely many cohomology sheaves of
$K$ to each stratum $S$ is, on quasi-compact pro-étale charts $U$, of
the form $\mathcal O_{E,U}\otimes_{\mathcal O_E}P$ with $P$ finitely
generated. Extension of scalars to $E_X$ is exact. So if $K[1/\ell]=0$,
then $E_U\otimes_{\mathcal O_E}P=0$, and each such $P$ is torsion.
Since the underlying space of $X$ is Noetherian, each stratum is
quasi-compact, so finitely many charts suffice. Since there are then finitely many $P$, one power of $\ell$ kills the restrictions of all
cohomology sheaves of $K$ to all strata. By the localization sequences of
Proposition [proposition-extension-zero-restriction-closed-subscheme], a larger power kills every cohomology
sheaf of $K$. Since $K$ is bounded, a further power kills $K$ itself,
by induction along its truncation triangles.

*Source:* the proof of Proposition [proposition-inverting-ell].
