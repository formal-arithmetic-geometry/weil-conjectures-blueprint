+++
id = "lem-wf-local-inertia-finite-parts"
kind = "lemma"
title = "The wild and non-$\\ell$ tame parts of the local monodromy are finite"
order = 2843
uses = ["d-real-boundary", "def-weil-pbc-scheme-conventions", "def-wf-fundamental-representation", "p-real-integral"]
+++
Let $\mathcal F$ be a lisse $\Qlb$-sheaf on a punctured smooth curve
over $k_0$ with $\operatorname{char}(k_0)=p\ne\ell$, and let
$V=\mathcal F_{\bar\eta}$ be a local geometric generic stalk at a
missing point, with the inertia action of
[def-wf-fundamental-representation]. For a boundary point $x$
with inertia group $I_x=P\rtimes I_x^{\mathrm{t}}$ of [d-real-boundary] (wild part $P$, a
pro-$p$-group, and tame part
$I_x^{\mathrm{t}}=\prod_{\ell'\ne p}\mathbf Z_{\ell'}(1)$), the images
of $P$ and of every $\mathbf Z_{\ell'}(1)$-factor with
$\ell'\ne\ell$ in $\operatorname{GL}(V)$ are finite.

## Proof

The image of a pro-$p$-group or pro-$\ell'$-group
($\ell'\ne\ell$) in $\operatorname{GL}(V)$ —the
fundamental-representation action on the local generic stalk in
[def-wf-fundamental-representation] —is a compact
pro-$p$- respectively pro-$\ell'$-subgroup $H$ of
$\operatorname{GL}(V)=\operatorname{GL}_n(\overline{\mathbf Q}_\ell)$.
Such an $H$ lies in a conjugate of
$\operatorname{GL}_n(\mathcal O_E)$ for a finite extension
$E/\mathbf Q_\ell$ (a compact subgroup of
$\operatorname{GL}_n(\overline{\mathbf Q}_\ell)$ stabilizes a lattice
after a finite extension, as in [p-real-integral]). The kernel of the reduction
$\operatorname{GL}_n(\mathcal O_E)\to\operatorname{GL}_n(\kappa)$
(with $\kappa$ the finite residue field of $E$) is a pro-$\ell$
group; $H\cap\ker$ is therefore simultaneously pro-$p$ (or
pro-$\ell'$) and pro-$\ell$, hence trivial: a group that is a
projective limit of finite groups all of whose orders are simultaneously
$p$-powers (respectively $\ell'$-powers) and $\ell$-powers is
trivial since $p\ne\ell\ne\ell'$. Hence $H\to\operatorname{GL}_n(\kappa)$
is injective, and its image is a subgroup of the finite group
$\operatorname{GL}_n(\kappa)$: $H$ is finite.
