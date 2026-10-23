+++
kind = "proof"
of = "lem-weil-pbc-filtered-colimit-normal-ring-domain"
uses = ["lem-weil-pbc-filtered-colimit-localization-at-prime"]
+++
Let $\mathfrak p\subset R$ be prime and $\mathfrak p_i\subset R_i$ its preimage. By [lem-weil-pbc-filtered-colimit-localization-at-prime], $R_{\mathfrak p}$ is the filtered colimit of the rings $(R_i)_{\mathfrak p_i}$, which are domains by hypothesis. $R_{\mathfrak p}$ is nonzero, being local. If $xy=0$ in $R_{\mathfrak p}$, represent $x,y$ by elements $x_i,y_i$ of a common $(R_i)_{\mathfrak p_i}$; as $x_iy_i$ maps to $0$, its image in some later $(R_j)_{\mathfrak p_j}$ is $0$, so the image of $x_i$ or of $y_i$ there is $0$ ($(R_j)_{\mathfrak p_j}$ being a domain), whence $x=0$ or $y=0$.
