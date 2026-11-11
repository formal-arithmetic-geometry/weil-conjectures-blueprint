+++
kind = "proof"
of = "lemma-bounds-finite-reductions--2"
order = 228005
uses = ["proposition-pro-etale-affines-form-basis", "definition-ind-etale-pro-etale-weakly--1", "definition-ind-etale-pro-etale-weakly--2", "proposition-etale-implications--1", "lemma-stability--3", "lemma-stability--7", "lemma-stability--8", "proposition-topos-functoriality--1", "proposition-pro-etale-affines-form-basis--1", "proposition-pro-etale-affines-form-basis--2", "lemma-reduction-derived-nakayama--1", "lemma-bounds-finite-reductions--1", "definition-sp-scalar-extension--2"]
+++
For the Tor bound we use
$K_n\otimes^{\mathbf L}_{\mathcal O_E/\pi_E^n}\mathbf F_E\simeq K_1$.
At an étale geometric point $\bar x$, take a bounded above resolution of the
stalk of $K_n$ by finite free modules over the Artinian local ring
$\mathcal O_E/\pi_E^n$. Cancelling a two-term identity summand whenever
a differential matrix has a unit entry, we obtain a minimal resolution.
Its differentials have entries in $(\pi_E)$, so they vanish after
tensoring with $\mathbf F_E$. Since stalks commute with derived tensor
products, the minimal resolution tensored with $\mathbf F_E$ computes the
stalk of $K_1$ at $\bar x$, with zero differential. Its rank
in degree $q$ is therefore $\dim_{\mathbf F_E}H^q(K_1)_{\bar x}$. This vanishes
outside $[a,b]$, and we conclude that the stalk has a bounded finite free
resolution in $[a,b]$. A bound on stalks gives the same Tor bound on the
étale site. Corollary [corollary-finite-tor-amplitude-under-comparison] carries
it to the pro-étale site, for Tor against arbitrary sheaves of modules there.

*Source:* the proof of Lemma [lemma-bounds-finite-reductions].
