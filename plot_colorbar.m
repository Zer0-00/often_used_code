function plot_colorbar(clim_needed,cmap,save_dir)
    hf = figure('Units','normalized','Visible','off'); 
    colormap(cmap)
    hCB = colorbar();
    set(gca,'Visible',false)
    set(gca,'CLim',clim_needed)
    hCB.Position = [0.3 0.15 0.4 0.74];
    hf.Position(3) = 0.1000;
    exportgraphics(hf,save_dir)
    close(hf)
end