+++
kind = "proof"
of = "lemma-p-torsion-affine-curve-characteristic--2"
uses = ["lemma-p-torsion-affine-curve-characteristic--3", "lemma-p-torsion-affine-curve-characteristic--4"]
+++
Write $q=n+2$. Let $K=\ker(\varphi-1:\mathbf G_a\to\mathbf G_a)$.
By [lemma-p-torsion-affine-curve-characteristic--3], the sequence
$0\to K\to\mathbf G_a\to\mathbf G_a\to0$ is short exact and
$\mathbf F_p\simeq K$. Its cohomology sequence contains

$$
H^{n+1}(U_{\acute{e}t},\mathbf G_a)\longrightarrow
H^{n+2}(U_{\acute{e}t},K)\longrightarrow
H^{n+2}(U_{\acute{e}t},\mathbf G_a).
$$

Both outer groups vanish by
[lemma-p-torsion-affine-curve-characteristic--4]. Exactness
(`CategoryTheory.Sheaf.H.exact_δSucc_map`) writes every element of the
middle group as the connecting image of zero, so the middle group
vanishes. Transport along $\mathbf F_p\simeq K$ gives the assertion.
