+++
kind = "proof"
of = "lemma-affine-covers-dense-intersection--2"
order = 1462004
uses = ["lemma-schematic-closure-uniqueness"]
+++
Choose an $S$-immersion $i:Y\hookrightarrow\mathbf A^n_S$ by
`AlgebraicGeometry.exists_immersion_affineSpace_of_quasiAffine`.
Compose it with the standard open immersion
$\mathbf A^n_S\hookrightarrow\mathbf P^n_S$ to obtain an immersion
$g:Y\to\mathbf P^n_S$. Since $f$ is quasi-compact and
$\mathbf P^n_S\to S$ is separated, $g$ is quasi-compact.

Take the scheme-theoretic image $\overline Y$ of $g$. Since $g$ is
a quasi-compact immersion, the induced map $j:Y\to\overline Y$ is
an open immersion, and
$\overline Y\hookrightarrow\mathbf P^n_S$ is a closed immersion.
The composite $p:\overline Y\to S$ is proper because
$\mathbf P^n_S\to S$ is proper. Thus $f=p\circ j$ is a
compactification; $j$ is quasi-compact because $f$ is quasi-compact
and $p$ is separated. This is the construction
`AlgebraicGeometry.Compactification.ofIsImmersionAffineSpace`, using
`AlgebraicGeometry.Compactification.ofIsImmersion` for the
scheme-theoretic image.

For a scheme of finite type over a Noetherian base, each affine open
$U_r$ in the cover is quasi-affine, and $U_r\to S$ is quasi-compact
and locally of finite type. The construction therefore supplies the
compactifications of the affine pieces used in Nagata's theorem.
