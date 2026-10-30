+++
kind = "proof"
of = "sk-prop-pbc-complete"
uses = ["sk-cor-pbc-proet-finite", "sk-def-pe-derived-completion", "det-pbc-complete-derived-completion", "lemma-weil-pbc-completed-pullback-reduction", "prop-weil-pbc-direct-image-limits", "det-pbc-complete-exchange-map", "det-pbc-complete-exchange-iso", "sk-cor-n-coefficient-quotients", "sk-def-exchange", "sk-lem-pbc-exchange-pasting"]
+++
We first compare reductions, then take their derived limit. The
projection formula map

$$
(Rp_*K)\otimes^{\mathbf L}(\mathcal O_E/\pi_E^n)_Y
\longrightarrow Rp_*K_n
$$

is the map in $D(Y_{\mathrm{pro}\acute{e}t},\mathcal O_E/\pi_E^n)$ whose adjoint is the
counit $p^*Rp_*K\to K$ tensored with the quotient. It is an isomorphism,
as may be checked after the conservative restriction of scalars to
$\mathcal O_E$. Indeed, $\mathcal O_E/\pi_E^n$ has the free resolution
$[\mathcal O_E\xrightarrow{\pi_E^n}\mathcal O_E]$, so by
Corollary [sk-cor-n-coefficient-quotients] both sides are the cone of
$\pi_E^n$ on $Rp_*K$, and $Rp_*$ is triangulated and $\mathcal O_E$-linear.
The resolutions for $n+1$ and $n$ are related by the chain map
$(\pi_E,\mathrm{id})$, and applying $Rp_*$ to it shows that these
comparisons form an isomorphism of towers. All these constructions can
be made on complexes with functorial resolutions, so the comparisons
define a map in the derived category of towers of
Definition [sk-def-pe-derived-completion].

Since $K$ is derived complete and $Rp_*$ is a right adjoint, we obtain

$$
Rp_*K\simeq Rp_*R\varprojlim_nK_n
\simeq R\varprojlim_nRp_*K_n.
$$

Together with the reduction comparisons, this proves that $Rp_*K$ is
derived complete. The definition of completed inverse image and the
same right-adjoint property for $Rp'_*$ now give

$$
\begin{aligned}
\hat g^*Rp_*K
&\simeq R\varprojlim_n g^*Rp_*K_n,\\
Rp'_*\hat g'^*K
&\simeq R\varprojlim_n Rp'_*g'^*K_n.
\end{aligned}
$$

The base change maps $g^*Rp_*K_n\to Rp'_*g'^*K_n$ are natural in $K_n$, so
they form a map of towers, and each is an isomorphism by
Theorem [sk-thm-properbasechange]. Its cone therefore has zero cohomology
at every level, and applying $R\varprojlim$ gives the asserted
isomorphism.

This isomorphism is compatible with the ordinary base change map. Both are
built from the counit of Definition [sk-def-exchange], and this counit is
natural with respect to the quotient maps and the chain maps
$(\pi_E,\mathrm{id})$. Hence the square formed by the ordinary base change
map $g^*Rp_*K\to Rp'_*g'^*K$, the completed one, and the completion maps
$g^*Rp_*K\to\hat g^*Rp_*K$ and $Rp'_*g'^*K\to Rp'_*\hat g'^*K$ commutes. If
$g^*Rp_*K$ and $g'^*K$ are derived complete, the completion maps are
isomorphisms, and the completed base change isomorphism is the ordinary
base change map. By Lemma [sk-lem-pbc-exchange-pasting] it is then
compatible with composition of base changes.
