+++
kind = "proof"
of = "sk-prop-ctf-finite-comparison"
uses = ["sk-prop-ctf-finite-compact"]
+++
The bounded finite-Tor comparison is [sk-cor-pe-finite-tor-comparison], and its unbounded full
faithfulness, coproduct preservation and direct-image comparison are [sk-prop-pe-unbounded-classical]. An
exact fully faithful coproduct-preserving functor identifies the localizing closures of corresponding
generators. The comparisons for pullback and extension by zero then give $Rf_!$ through a
compactification ([det-ctf-finite-comparison-localizing]).

For the equality with the whole étale derived category, let $u\colon U\to X$ range over a basis of
quasi-compact separated étale objects. The free representable module sheaves $u_!A_U$ are flat
constructible, hence belong to $\Dctf(X_{\mathrm{ét}},A)$, and their shifts detect zero objects of
$\D(X_{\mathrm{ét}},A)$ through derived sections on $U$. The étale part of the proof of
[sk-prop-ctf-finite-compact] shows that they are compact in all of $\D(X_{\mathrm{ét}},A)$: it uses local
support, continuity and cohomological dimension, which hold for them. By the standard compact-generation
theorem, their localizing closure is the entire étale derived category
([det-ctf-finite-comparison-whole]).
