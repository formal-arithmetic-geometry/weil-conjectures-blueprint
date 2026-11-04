+++
kind = "proof"
of = "proposition-proper-base-change-complete-integral"
order = 413
uses = ["corollary-finite-quotients-their-transition-maps", "theorem-proper-base-change-classical-pro"]
+++
Theorem [theorem-proper-base-change-classical-pro] applies at each
finite level, so the point is that $Rp_*$ and the completed inverse
images are compatible with the passage to the derived limit of the
reductions.

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
isomorphism, and $Rp_*K$ is derived complete. The definition of completed
inverse image and the same right-adjoint property for $Rp'_*$ now give

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
Theorem [theorem-proper-base-change-classical-pro]. Its cone therefore has zero cohomology
at every level, and applying $R\varprojlim$ gives the asserted
isomorphism.
