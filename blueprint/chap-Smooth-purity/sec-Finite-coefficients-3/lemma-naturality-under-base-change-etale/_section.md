+++
id = "lemma-naturality-under-base-change-etale"
kind = "lemma"
title = "Naturality under base change and étale maps"
order = 752
uses = ["definition-constructible-sheaves", "proposition-exceptional-inverse-image-smooth-morphism", "definition-deformation-normal-bundle", "definition-compactification-refinement"]
+++
Write $\alpha_{g,s}:s^*\href{@definition-relative-dualizing-complex}{\omega_g}\xrightarrow{\sim}z^*\href{@definition-relative-dualizing-complex}{\omega_\pi}$
for the comparison of Lemma [lemma-section-normal-bundle].

1. Let $h:S'\to S$ be any morphism for which the schemes below
   satisfy the standing hypotheses. Put $V'=V\times_SS'$, and denote
   the base changes of the maps by $g',s',\pi',z'$. There are canonical
   identifications
   $$
   N_{s'}\simeq N_s\times_SS',\qquad
   \href{@definition-deformation-normal-bundle}{\mathcal D_{s'(S')}V'}
   \simeq\href{@definition-deformation-normal-bundle}{\mathcal D_{s(S)}V}\times_SS'.
   $$
   Under these identifications and the [exceptional base change
   isomorphisms](@definition-exceptional-base-change-map) of Proposition [proposition-exceptional-inverse-image-smooth-morphism](3), the
   following square commutes:
   $$
   \begin{CD}
   h^*s^*\href{@definition-relative-dualizing-complex}{\omega_g} @>{h^*\alpha_{g,s}}>> h^*z^*\href{@definition-relative-dualizing-complex}{\omega_\pi}\\
   @V{\sim}VV @VV{\sim}V\\
   (s')^*\href{@definition-relative-dualizing-complex}{\omega_{g'}} @>{\alpha_{g',s'}}>> (z')^*\href{@definition-relative-dualizing-complex}{\omega_{\pi'}}.
   \end{CD}
   $$
2. Let $e:V'\to V$ be an étale $S$-morphism and let
   $s':S\to V'$ be a closed section such that $es'=s$ and
   $e^{-1}(s(S))=s'(S)$ scheme-theoretically. Put $g'=ge$.
   The induced map $N_{s'}\to N_s$ is a linear isomorphism, and the
   induced map of [deformation spaces](@definition-deformation-normal-bundle) is étale. The identifications
   $$
   (s')^*\href{@definition-relative-dualizing-complex}{\omega_{g'}}\simeq s^*\href{@definition-relative-dualizing-complex}{\omega_g},\qquad
   (z')^*\href{@definition-relative-dualizing-complex}{\omega_{\pi'}}\simeq z^*\href{@definition-relative-dualizing-complex}{\omega_\pi}
   $$
   obtained by composing adjunctions carry $\alpha_{g',s'}$ to
   $\alpha_{g,s}$.

These comparisons respect identities, composition and interchange of
base change with an étale map of pairs.
