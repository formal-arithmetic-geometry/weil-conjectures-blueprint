+++
id = "lem-weil-pbc-free-resolution-ses-split"
kind = "lemma"
title = "A short exact sequence of modules has a degreewise split short exact sequence of free resolutions"
lean = ["Module.exists_free_resolution_ses_split"]
order = 1920
+++
Let $R$ be a commutative ring and $0\to Q\xrightarrow{u}Q'\xrightarrow{v}Q''\to0$ a short exact sequence of $R$-modules ($u$ injective, $\ker v=\operatorname{im}u$, $v$ surjective). Then there exist chain complexes of free $R$-modules $F_\bullet$, $F'_\bullet$, $F''_\bullet$ (indexed by $n\ge0$, differentials $d,d',d''$) with $R$-linear augmentations $\varepsilon:F_0\to Q$, $\varepsilon':F'_0\to Q'$, $\varepsilon'':F''_0\to Q''$ such that the three augmented complexes $\cdots\to F_1\xrightarrow{d_1}F_0\xrightarrow{\varepsilon}Q\to0$, $\cdots\to F'_1\to F'_0\xrightarrow{\varepsilon'}Q'\to0$, $\cdots\to F''_1\to F''_0\xrightarrow{\varepsilon''}Q''\to0$ are exact (free resolutions), together with morphisms of complexes $\alpha:F_\bullet\to F'_\bullet$, $\beta:F'_\bullet\to F''_\bullet$ ($d'_n\alpha_n=\alpha_{n-1}d_n$, $d''_n\beta_n=\beta_{n-1}d'_n$) satisfying $\varepsilon'\alpha_0=u\varepsilon$ and $\varepsilon''\beta_0=v\varepsilon'$, and, for every $n\ge0$, $R$-linear maps $\pi_n:F'_n\to F_n$ and $s_n:F''_n\to F'_n$ (not required to commute with the differentials) with $\beta_n\alpha_n=0$, $\pi_n\alpha_n=\mathrm{id}_{F_n}$, $\beta_ns_n=\mathrm{id}_{F''_n}$ and $\alpha_n\pi_n+s_n\beta_n=\mathrm{id}_{F'_n}$. In particular $0\to F_n\xrightarrow{\alpha_n}F'_n\xrightarrow{\beta_n}F''_n\to0$ is split exact for every $n$.
