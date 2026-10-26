+++
id = "def-weil-pbc-analytically-unramified"
kind = "definition"
title = "Analytically unramified local rings and primes"
lean = ["IsAnalyticallyUnramified", "Ideal.IsAnalyticallyUnramified"]
order = 1603
+++
Let $(A,\mathfrak m)$ be a Noetherian local ring. The ring $A$ is *analytically unramified* when its $\mathfrak m$-adic completion $\widehat A=\varprojlim_n A/\mathfrak m^n$ is reduced, meaning it has no nonzero nilpotent element. A prime ideal $\mathfrak p\subseteq A$ is *analytically unramified* when the $\mathfrak m/\mathfrak p$-adic completion of $A/\mathfrak p$ is reduced, that is, when the local ring $A/\mathfrak p$, with maximal ideal $\mathfrak m/\mathfrak p$, is analytically unramified.
