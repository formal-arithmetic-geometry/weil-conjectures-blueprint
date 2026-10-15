+++
kind = "proof"
of = "sk-lem-sp-tower"
uses = ["sk-prop-pe-replete"]
+++
Let $C=R\varprojlim_nC_n$ (Stacks, Tag 0940). Reduction modulo $\ell^m$ is the
cone of $\ell^m$, so it commutes with $R\varprojlim$. Fix $m$; the terms with
$n<m$ do not affect the derived limit. For $n\geq m$,
$\mathcal O_{E,T}/\ell^n\otimes^{\mathbf L}_{\mathcal O_{E,T}}\mathcal O_{E,T}/\ell^m$
has $H^0=H^{-1}=\mathcal O_{E,T}/\ell^m$. Its truncation triangle and
normalization give triangles

$$
C_m[1]\longrightarrow C_n\otimes^{\mathbf L}_{\mathcal O_{E,T}}\mathcal O_{E,T}/\ell^m\longrightarrow C_m,
$$

in which the transition maps on the left term are multiplication by powers of
$\ell$, hence zero along the indices $m,2m,3m,\dots$; so the left term has
vanishing $R\varprojlim$, and the reduction formula follows. The complex $C$ is
derived complete as a limit of complexes killed by powers of $\ell$, and it is
bounded since $T_{\mathrm{proét}}$ is replete ([sk-prop-pe-replete]). Since
$C/\ell\simeq C_1$ lies in $\Dctf(T_{\mathrm{proét}},\mathcal O_E/\ell)$, $C$ lies in
$\Dbc(T,\mathcal O_E)$ by the characterization of integral constructible
complexes in the set-up of the smooth purity section (a derived complete $K$
with $K/\ell$ in $\Dctf$ is in $\Dbc(T,\mathcal O_E)$). The same calculation of
normalized towers is in Bhatt–Scholze, Lemmas 3.5.4–3.5.7, and Stacks, Tag
099P.
