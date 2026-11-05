+++
kind = "proof"
of = "proposition-proper-base-change-complete-integral--1"
order = 417002
uses = ["definition-ind-etale-pro-etale-weakly--1", "definition-ind-etale-pro-etale-weakly--2", "proposition-etale-implications--1", "lemma-stability--4", "lemma-stability--6", "lemma-stability--7", "proposition-topos-functoriality--1", "definition-w-local-w-strictly-local--2", "definition-w-local-w-strictly-local--3", "proposition-w-local-components--1", "proposition-pro-etale-affines-form-basis--2", "lemma-reduction-derived-nakayama--1", "proposition-sp-unique-adjoint--1"]
+++
The reductions of $Rp_*K$ are controlled by the projection formula. The
projection formula map (4.14) for
$M=(\mathcal O_E/\pi_E^n)_Y$ is a map

$$
(Rp_*K)\otimes^{\mathbf L}(\mathcal O_E/\pi_E^n)_Y
\longrightarrow Rp_*K_n,
$$

which we regard in $D(Y_{\mathrm{pro}\acute{e}t},\mathcal O_E/\pi_E^n)$. We claim that it is an
isomorphism. Restriction of scalars to $\mathcal O_E$ is conservative, so
we may check this after forgetting the $\mathcal O_E/\pi_E^n$-structure.
The ring $\mathcal O_E/\pi_E^n$ has the free resolution
$[\mathcal O_E\xrightarrow{\pi_E^n}\mathcal O_E]$. By
Corollary [corollary-finite-quotients-their-transition-maps], the source is therefore the cone of
$\pi_E^n$ on $Rp_*K$, and the target is $Rp_*$ of the cone of $\pi_E^n$ on
$K$. These agree because $Rp_*$ is triangulated and $\mathcal O_E$-linear.
The resolutions for $n+1$ and $n$ are related by the chain map
$(\pi_E,\mathrm{id})$, and applying $Rp_*$ to it shows that these
comparisons form an isomorphism of towers. All these constructions can
be made on complexes with functorial resolutions, so the comparisons
define a map in the derived category of towers of
Definition [definition-derived-adic-completeness].

Since $K$ is derived complete, it is the derived
limit of its reductions $K_n$. The functor $Rp_*$ is a right adjoint, so it
commutes with derived limits, and we obtain

$$
Rp_*K\simeq Rp_*R\varprojlim_nK_n
\simeq R\varprojlim_nRp_*K_n.
$$

By the reduction comparisons, the right side is the derived limit of the
reductions $(Rp_*K)\otimes^{\mathbf L}(\mathcal O_E/\pi_E^n)_Y$, that is,
the derived completion of $Rp_*K$. Hence the completion map of $Rp_*K$ is an
isomorphism, and $Rp_*K$ is derived complete.

*Source:* the proof of Proposition [proposition-proper-base-change-complete-integral].
