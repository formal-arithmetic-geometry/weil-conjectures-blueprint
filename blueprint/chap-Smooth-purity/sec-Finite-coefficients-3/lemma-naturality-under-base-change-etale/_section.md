+++
id = "lemma-naturality-under-base-change-etale"
kind = "lemma"
title = "Naturality under base change and étale maps"
order = 751
uses = ["lemma-section-normal-bundle"]
+++
Write $\alpha_{g,s}:s^*\omega_g\xrightarrow{\sim}z^*\omega_\pi$
for the comparison of Lemma [lemma-section-normal-bundle].

1. Let $h:S'\to S$ be any morphism for which the schemes below
   satisfy the standing hypotheses. Put $V'=V\times_SS'$, and denote
   the base changes of the maps by $g',s',\pi',z'$. There are canonical
   identifications
   $$
   N_{s'}\simeq N_s\times_SS',\qquad
   \mathcal D_{s'(S')}V'
   \simeq\mathcal D_{s(S)}V\times_SS'.
   $$
   Under these identifications and the exceptional base change
   isomorphisms of Proposition [proposition-exceptional-inverse-image-smooth-morphism](3), the
   following square commutes:
   $$
   \begin{CD}
   h^*s^*\omega_g @>{h^*\alpha_{g,s}}>> h^*z^*\omega_\pi\\
   @V{\sim}VV @VV{\sim}V\\
   (s')^*\omega_{g'} @>{\alpha_{g',s'}}>> (z')^*\omega_{\pi'}.
   \end{CD}
   $$
2. Let $e:V'\to V$ be an étale $S$-morphism and let
   $s':S\to V'$ be a closed section such that $es'=s$ and
   $e^{-1}(s(S))=s'(S)$ scheme-theoretically. Put $g'=ge$.
   The induced map $N_{s'}\to N_s$ is a linear isomorphism, and the
   induced map of deformation spaces is étale. The identifications
   $$
   (s')^*\omega_{g'}\simeq s^*\omega_g,\qquad
   (z')^*\omega_{\pi'}\simeq z^*\omega_\pi
   $$
   obtained by composing adjunctions carry $\alpha_{g',s'}$ to
   $\alpha_{g,s}$.

These comparisons respect identities, composition and interchange of
base change with an étale map of pairs.
