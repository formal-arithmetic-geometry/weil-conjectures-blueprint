+++
kind = "proof"
of = "lemma-bounds-finite-reductions--1"
order = 228003
uses = ["proposition-pro-etale-affines-form-basis", "definition-ind-etale-pro-etale-weakly--1", "definition-ind-etale-pro-etale-weakly--2", "proposition-etale-implications--1", "lemma-stability--3", "lemma-stability--6", "lemma-stability--7", "lemma-stability--8", "proposition-pro-etale-coverings--2", "proposition-topos-functoriality--1", "lemma-extremally-disconnected-covers--3", "proposition-pro-etale-affines-form-basis--1", "proposition-pro-etale-affines-form-basis--2", "proposition-comparison-morphism-inverse-image--1", "proposition-comparison-morphism-inverse-image--2", "proposition-comparison-morphism-inverse-image--3", "theorem-classical-sheaves-essential-image--1", "theorem-bounded-below-cohomology-comparison--1", "theorem-bounded-below-cohomology-comparison--2", "proposition-comparison-immersions--1", "proposition-comparison-immersions--2", "proposition-locally-constant-sheaves-finite-presentation--3", "definition-constructible-sheaves--2", "definition-constructible-sheaves--5", "definition-constructible-sheaves--6", "proposition-comparison-etale-derived-category--5", "definition-compactification-refinement--1"]
+++
The filtration of $\mathcal O_E/\pi_E^n$ by the powers of $\pi_E$ has
graded pieces $\mathbf F_E$. Tensoring its short exact sequences with
$K$ over $\mathcal O_{E,X}$, we get triangles
$K_1\to K_{n}\to K_{n-1}$, up to the identification
$\pi_E^{n-1}\mathcal O_E/\pi_E^n\simeq\mathbf F_E$. Complexes with
constructible cohomology in $[a,b]$ are closed under extensions in
triangles. This follows from the long exact cohomology sequence and the fact
that constructible sheaves form a weak Serre subcategory. Induction on $n$ now shows
that $K_n$ is bounded in $[a,b]$ with constructible cohomology. Locally constant
finite sheaves of modules also form a weak Serre subcategory. Hence the same
induction works on a fixed stratum, and a single stratification works for
all $n$. By the comparison theorem for constructible sheaves
(Theorem [theorem-comparison-constructible-sheaves]), these finite sheaves and
complexes are classical, that is, pulled back from the étale site.

*Source:* the proof of Lemma [lemma-bounds-finite-reductions].
