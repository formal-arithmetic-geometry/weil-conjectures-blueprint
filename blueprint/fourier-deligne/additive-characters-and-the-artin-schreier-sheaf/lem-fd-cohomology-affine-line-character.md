+++
id = "lem-fd-cohomology-affine-line-character"
kind = "lemma"
title = "Cohomology of an affine line with an exponential sheaf"
order = 4145
uses = ["lem-fd-affine-line-constant-cohomology", "lem-fd-as-characters", "lem-fd-as-cover-affine-line", "lem-fd-as-lisse", "lem-fd-finite-pushforward-cohomology"]
+++
Let $k$ be finite or algebraically closed, let $a\in k$, and let $\psi_a(x)=\psi(ax)$. Over $\mathbf A^1_k$,

$$
H^q(\mathbf A^1_{\bar k},\mathcal L_{\psi_a})=\begin{cases}\overline{\mathbf Q}_\ell,&q=0,\ a=0,\\0,&\text{otherwise.}\end{cases}
$$

## Proof

The covering $\pi:\mathbf A^1_y\to\mathbf A^1_x$, $x=y^p-y$, of [lem-fd-as-cover-affine-line] is finite, so by [lem-fd-finite-pushforward-cohomology] and the isotypic decomposition of [lem-fd-as-characters],

$$
\bigoplus_{\chi\in\widehat{\mathbf F}_p}H^q(\mathbf A^1_x,\mathcal L_\chi)\cong H^q(\mathbf A^1_x,\pi_*\overline{\mathbf Q}_\ell)\cong H^q(\mathbf A^1_y,\overline{\mathbf Q}_\ell),
$$

which is $\overline{\mathbf Q}_\ell$ in degree $0$ and $0$ above by [lem-fd-affine-line-constant-cohomology]. The $\mathbf F_p$-action of [lem-fd-as-cover-affine-line], $y\mapsto y+a$, acts trivially on $H^0(\mathbf A^1_y,\overline{\mathbf Q}_\ell)$ (the automorphism pulls back the constant sheaf to itself), so in degree $0$ only the component $\chi=0$ survives, and the component $\chi=0$ is the constant sheaf (the deck-invariant subsheaf of $\pi_*\overline{\mathbf Q}_\ell$). The sheaf $\mathcal L_{\psi_a}$ is lisse of rank one and not constant for $a\neq0$ ([lem-fd-as-lisse] and the definiteness of the character $\psi_a$), so it is one of the components $\mathcal L_\chi$ with $\chi\neq0$, and all its cohomology vanishes; for $a=0$, $\mathcal L_{\psi_0}$ is the constant component and [lem-fd-affine-line-constant-cohomology] gives $\overline{\mathbf Q}_\ell$ in degree $0$ and $0$ above.
