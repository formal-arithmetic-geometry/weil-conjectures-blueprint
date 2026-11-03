+++
kind  = "proof"
of    = "lem-weil-pbc-constructible-finite-pushforward-approximation"
uses  = ["lem-weil-pbc-constructible-finite-pushforward-noetherian"]
+++
*Step 1: the approximation.* A quasi-compact quasi-separated scheme is the
inverse limit $U=\varprojlim_\lambda U_\lambda$ of schemes of finite type over
$\mathbf Z$ (in particular Noetherian) with affine transition maps (absolute
Noetherian approximation, Stacks Project, Limits of Schemes, Tag
[01ZA](https://stacks.math.columbia.edu/tag/01ZA)).

*Step 2: the sheaf descends.* Constructibility of $C$ gives a finite partition
of $U$ into constructible locally closed subschemes on each of which $C$ is
finite locally constant with finitely generated (hence, $\Lambda$ being
Noetherian, finitely presented) values. Such a sheaf is specified by finitely
many etale objects of finite presentation, finitely many sections and finitely
many relations expressing the trivializations, the module structures and the
compatibilities on overlaps. By descent of finite-presentation data at an
inverse limit with affine transition maps, all of this descends to one stage
$U'=U_\lambda$: there is a constructible sheaf of $\Lambda$-modules $C'$ on
$U'_{\Et}$ with $\nu^{-1}C'\cong C$, where $\nu:U\to U'$ is the projection.

*Step 3: the embedding on the Noetherian stage.* Apply
[lem-weil-pbc-constructible-finite-pushforward-noetherian] to $C'$ on the
Noetherian scheme $U'$: there are finite morphisms $h_i:V_i\to U'$ and finitely
generated $\Lambda$-modules $M_i$ with a monomorphism
$C'\hookrightarrow\bigoplus_i(h_i)_*\underline{M_i}$. Since $U'$ is Noetherian,
every finite morphism $h_i$ is of finite type, hence of finite presentation,
in particular locally of finite presentation.
