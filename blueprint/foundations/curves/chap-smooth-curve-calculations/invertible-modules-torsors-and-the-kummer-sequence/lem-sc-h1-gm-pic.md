+++
id = "lem-sc-h1-gm-pic"
kind = "lemma"
title = "The Picard group as first cohomology of units"
order = 2159
uses = ["def-sc-curves", "def-sc-gm-torsor", "def-sc-invertible-module", "def-sc-picard-group", "lem-sc-line-bundle-torsor", "lem-sc-torsor-h1"]
+++
Let $C$ be a curve. There is a
canonical isomorphism of abelian groups

$$
H^1(C_{\Et},\mathbf G_m)\cong\operatorname{Pic}(C),
$$

sending the class of an
invertible module $\mathcal L$
to the torsor $\underline{\operatorname{Isom}}(\mathcal O_C,\mathcal L)$.

## Proof

By [lem-sc-torsor-h1] applied to $G=\mathbf G_m$,
$H^1(C_{\Et},\mathbf G_m)$ is canonically the group of
isomorphism classes of $\mathbf G_m$-torsors, and by
[lem-sc-line-bundle-torsor] those are canonically
$\operatorname{Pic}(C)$ ([def-sc-picard-group]). The
composition is the stated map. (This proves *Stacks Project,
Lemma 21.6.1, Tag [040E](https://stacks.math.columbia.edu/tag/040E)*,
in Section 21.6: for a (locally) ringed site,
$H^1(\mathcal C,\mathcal O^*)=\operatorname{Pic}(\mathcal O)$.)
