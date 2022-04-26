const path = require('path');
const {WebpackManifestPlugin} = require('webpack-manifest-plugin');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');


module.exports = {
    devtool: "source-map",
    entry: {
        calendar: '/src/calendar.js',
        style: '/src/style.scss'
        },
    output: {
        filename: '[name].[contenthash].js',
        publicPath: '/static/dist/',
        path: path.resolve(__dirname, 'opv2', 'static', 'dist'),
        clean: true
    },
    module: {
        rules: [{
            test: /\.scss$/,
            use: [
                MiniCssExtractPlugin.loader,
                {
                    loader: 'css-loader'
                },
                {
                    loader: 'sass-loader',
                    options: {
                        sourceMap: true,
                    }
                }
            ]
        },
        {
        test: /\.css$/i,
        use: [MiniCssExtractPlugin.loader, "css-loader"],
        },
        ]},
    plugins: [
        new WebpackManifestPlugin(),
        new MiniCssExtractPlugin({
            filename: '[name].[contenthash].css'
        })
    ]
};