+++
kind  = "proof"
of    = "cor-sf-direct-image-ctf-proetale"
+++
By [lem-sf-proetale-constructible-origin] the object $K$ is of
étale origin: there are a bounded complex $K'$ with constructible
cohomology on $X_{\Et}$ and an isomorphism $K\cong\nu_X^*K'$, and by
[lem-sf-comparison-tor-amplitude](ii) the complex $K'$ has finite Tor
amplitude in $[a,b]$ on the étale site.
[cor-sf-direct-image-ctf-nonproper], whose two inputs are
[thm-sf-direct-image-tor-amplitude] and
[lem-sf-etale-direct-image-vanishing], therefore gives a bounded
constructible étale complex $Rf_{\Et,*}K'$ with finite Tor amplitude in
$[a,b+2d]$. The morphism $f$ is of finite type, hence quasi-compact and
quasi-separated, so the comparison direct image of
[prop-weil-pbc-comparison-direct-image] gives an isomorphism

$$
Rf_{\Proet,*}\nu_X^*K'\cong\nu_Y^*Rf_{\Et,*}K',
$$

and [lem-sf-comparison-tor-amplitude](i) gives finite Tor amplitude in
$[a,b+2d]$ and bounded constructibility for the right-hand side. As in
[cor-sf-direct-image-ctf-etale-origin] this is clause (iii) of
the finite-Tor preservation summary at the finite coefficient stage $A$ for the
object $K$.
