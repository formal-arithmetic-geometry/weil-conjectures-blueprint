+++
kind  = "proof"
of    = "lem-kun-sep-closure-conservative"
+++
Let $\bar x:\Spec(\Omega)\to X$ be a geometric point; $\Omega$ is
algebraically closed and contains $\kappa(x)$, hence contains the
algebraic closure of $K$, in particular $K^{\mathrm{sep}}$, so
$\bar x$ factors as
$\Spec(\Omega)\to X_{K^{\mathrm{sep}}}\to X$. If $\alpha$ becomes
an isomorphism after pullback to $X_{K^{\mathrm{sep}}}$, then its
stalk at $\bar x$ (the pullback along $\bar x$, see
[lem-kun-stalk-as-pullback]) is an isomorphism as it factors
through the pullback along
$\Spec(\Omega)\to X_{K^{\mathrm{sep}}}$; all stalks are
isomorphic, so $\alpha$ is an isomorphism by
[lemma-weil-pbc-geometric-stalk-conservative] (and
[lem-kun-stalk-faithful-derived] in the derived case).
