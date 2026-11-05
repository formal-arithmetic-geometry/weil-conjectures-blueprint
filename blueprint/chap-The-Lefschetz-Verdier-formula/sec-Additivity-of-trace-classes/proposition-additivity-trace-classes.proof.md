+++
kind = "proof"
of = "proposition-additivity-trace-classes"
order = 943
uses = ["theorem-comparison-direct-images", "definition-pro-etale-base-change-map", "definition-projection-formula-map", "lemma-change-coefficients", "lemma-external-duality-trace-morphism", "definition-trace-morphism", "lemma-lift-correspondence-invariant-decomposition", "lemma-closed-piece-pushforward"]
+++
For (1), the section $A_C\to\cHom_F(c_2^*\mathcal K,c_1^!\mathcal K)$
defined by $\tilde u$ comes from the unit in weight zero, so it lands in
$F^0$, and its image in $\operatorname{gr}^0$ is the tuple $(u_a)_a$.
Composing with the filtered trace morphism of
Lemma [lemma-filtered-trace-morphism] and forgetting the filtration
gives on the one hand $\operatorname{Tr}_c(u)$, and on the other hand,
by the factorization through $\operatorname{gr}^0$, the sum of the trace
classes $\operatorname{Tr}_c(u_a)$. For (2) we apply (1) to the lift
$\tilde u$ of Lemma [lemma-lift-correspondence-invariant-decomposition].
