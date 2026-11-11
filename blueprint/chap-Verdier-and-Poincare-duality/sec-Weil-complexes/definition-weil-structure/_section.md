+++
id = "definition-weil-structure"
kind = "definition"
title = "Weil structure"
order = 876
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-topos-functoriality", "example-locally-constant-functions-w-local", "proposition-comparison-morphism-inverse-image", "lemma-inverse-image-coefficient-sheaves", "definition-constructible-sheaves", "lemma-constructible-sheaves", "lemma-integral-models"]
+++
For $K\in D^b_{\mathrm{ctf}}(T,\Lambda)$, a *Weil structure*
is an isomorphism

$$
\phi_K:\operatorname{Fr}_T^*K\xrightarrow{\sim}K.
$$

A *Weil complex* is a pair $(K,\phi_K)$ with this structure.
A morphism $(K,\phi_K)\to(L,\phi_L)$ is a morphism
$h:K\to L$ satisfying

$$
h\circ\phi_K=\phi_L\circ\operatorname{Fr}_T^*(h).
$$
