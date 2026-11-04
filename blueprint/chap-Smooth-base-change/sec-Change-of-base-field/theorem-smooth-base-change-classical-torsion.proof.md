+++
kind = "proof"
of = "theorem-smooth-base-change-classical-torsion"
order = 684
uses = ["theorem-comparison-direct-images", "lemma-degree-zero-calculation", "lemma-reduction-curve-over-normal-base", "proposition-base-change-larger-algebraically-closed"]
+++
We argue by induction on $q$. The degree-zero calculation starts the
induction. By the reductions above, a hypothetical failure in degree $q$
gives a nonzero sheaf $R^qh_*\underline{\mathbf Z/m}$, and
Proposition [proposition-base-change-larger-algebraically-closed]
says that this sheaf is zero.

A smooth morphism is flat, locally of finite presentation, and has
geometrically reduced fibres, and so the case of degree zero is
Lemma [lemma-degree-zero-calculation]. Let $q\geq1$ and assume the theorem in
all degrees less than $q$. Fix $n$ invertible on $Y$. Since smoothness is
stable under base change, we may apply the induction hypothesis after
every base change $T\to Y$, which shows that $\mathrm{BC}(g,n,q-1)$ holds. By étale
coordinates and composition of base change maps, it suffices to treat the case
where $g$ is affine and smooth of relative dimension one.

If $\mathrm{BC}(g,n,q)$ failed, Lemma [lemma-reduction-curve-over-normal-base]
would give $S$, $C$, $h$ and $m$ with $R^qh_*\underline{\mathbf Z/m}\neq0$.
The hypotheses of
Proposition [proposition-base-change-larger-algebraically-closed] hold.
By construction $S$ is the spectrum of a normal domain with algebraically
closed fraction field. Since $m$ divides $n$, it is invertible on $S$. And
$C$ is a smooth affine curve over $S$. The conclusion
$R^qh_*\underline{\mathbf Z/m}=0$ of the proposition is a contradiction.
Hence $\mathrm{BC}(g,n,q)$ holds for affine $g$ of relative dimension one,
and by the reduction above it holds for every smooth $g$.

Since $f$ and $f'$ are qcqs, both sides commute with the filtered union
$F=\bigcup_nF[n]$. This gives the theorem for $F$ on the étale sites.
Theorem [theorem-comparison-direct-images] transfers the isomorphism and
the base change map from the étale sites to $Y'_{\mathrm{pro}\acute{e}t}$.
