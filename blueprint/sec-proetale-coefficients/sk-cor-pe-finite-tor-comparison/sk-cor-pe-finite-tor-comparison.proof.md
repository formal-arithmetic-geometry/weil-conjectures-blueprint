+++
kind = "proof"
of = "sk-cor-pe-finite-tor-comparison"
uses = ["lem-exc-constant-inverse-image-flat", "lem-exc-comparison-tor-interval", "det-pe-finite-tor-comparison-noetherian"]
+++
The ring map for $\nu_X$ is an isomorphism, and inverse image is exact and
symmetric monoidal. Pullback of flat module sheaves is flat (Stacks Project, Tag
05VD; [lem-exc-constant-inverse-image-flat]), so the pullback of a bounded flat
resolution preserves the Tor bound. Conversely, let $K$ be an étale complex and
test $K\otimes_\Lambda^{\mathrm L}M$ against arbitrary étale module sheaves $M$.
Its inverse image is $\nu_X^*K\otimes_{\Lambda_X}^{\mathrm L}\nu_X^*M$, and since
$\nu_X^*$ is exact and fully faithful it detects vanishing of cohomology; so a Tor
bound on $\nu_X^*K$ gives the same bound on $K$
([lem-exc-comparison-tor-interval], [lem-exc-comparison-tor-interval],
[det-pe-finite-tor-comparison-noetherian]). For constructible complexes the bound
can equivalently be checked on stalk complexes on each stratum.
