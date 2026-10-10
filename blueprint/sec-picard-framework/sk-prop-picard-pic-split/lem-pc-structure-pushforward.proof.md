+++
kind  = "proof"
of    = "lem-pc-structure-pushforward"
+++
Since $X$ is proper over $k$, $f_T$ is proper, hence quasi-compact and
quasi-separated, so $f_{T,*}\mathcal{O}_{X_T}$ is quasi-coherent
([lem-pc-finite-support-hi](1)). To identify it with $\mathcal{O}_T$ it
suffices to show that its sections over every affine open
$V=\operatorname{Spec}(A)\subseteq T$ equal $A$ compatibly with localization: by
[lem-sc-flat-base-change-coherent] applied to $X$ proper over $k$,
the flat $k$-algebra $A$ and $\mathcal{F}=\mathcal{O}_X$,

$$
\Gamma(X_V,\mathcal{O}_{X_V})=H^0(X_V,\mathcal{O}_{X_V})\cong H^0(X,\mathcal{O}_X)\otimes_kA
=k\otimes_kA=A ,
$$

and these identifications are compatible with the localization maps of
the structure sheaf of $T$ (the corresponding identification holds for
every localizing $A\to A_f$). Hence $f_{T,*}\mathcal{O}_{X_T}=\mathcal{O}_T$.
