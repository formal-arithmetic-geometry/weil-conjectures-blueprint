+++
kind = "proof"
of = "lem-weil-pbc-lift-to-injective-unique-up-to-homotopy"
uses = ["def-sp-abelian", "def-sp-injective-resolutions", "def-weil-abstract-derived-category"]
+++
Since $I^\bullet$ is bounded below with injective terms, it is K-injective: every morphism from an acyclic complex to $I^\bullet$ is null-homotopic. ([def-sp-injective-resolutions]).

Chain-homotopic maps become equal in the derived category, so $\beta_1\circ\alpha$ and $\beta_2\circ\alpha$ have the same image there. Since $\alpha$ is a quasi-isomorphism, its image in the derived category is an isomorphism; cancelling it shows that the images of $\beta_1$ and $\beta_2$ in the derived category agree. ([def-sp-abelian], [def-weil-abstract-derived-category]).

For a K-injective target $I^\bullet$, the localization map from morphisms $L^\bullet\to I^\bullet$ in the homotopy category to morphisms in the derived category is bijective. Hence $\beta_1$ and $\beta_2$ are already equal in the homotopy category, i.e. they are chain-homotopic, which gives the required maps $k^n$. ([def-weil-abstract-derived-category]).
