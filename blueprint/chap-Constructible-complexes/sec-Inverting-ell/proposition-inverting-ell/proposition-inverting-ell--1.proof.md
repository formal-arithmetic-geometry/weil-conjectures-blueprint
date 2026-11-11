+++
kind = "proof"
of = "proposition-inverting-ell--1"
order = 303002
uses = ["proposition-pro-etale-affines-form-basis", "definition-ind-etale-pro-etale-weakly--1", "definition-ind-etale-pro-etale-weakly--2", "proposition-etale-implications--1", "lemma-stability--3", "lemma-stability--6", "lemma-stability--7", "lemma-stability--8", "proposition-pro-etale-coverings--2", "proposition-topos-functoriality--1", "definition-w-local-w-strictly-local--4", "lemma-extremally-disconnected-covers--3", "proposition-splitting-ind-etale-covers--1", "theorem-existence-contractible-covers--1", "theorem-pro-etale-refinements-weakly-etale--1", "proposition-pro-etale-affines-form-basis--1", "proposition-pro-etale-affines-form-basis--2", "lemma-w-contractible-affines-projective--1", "definition-weak-contractibility--1", "lemma-inverse-image-coefficient-sheaves--1", "lemma-acyclic-resolutions--1", "proposition-sp-unique-adjoint--1"]
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
